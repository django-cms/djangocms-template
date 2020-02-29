from typing import Optional

from aldryn_apphooks_config.mixins import AppConfigMixin
from aldryn_apphooks_config.utils import get_app_instance
from django.db.models import QuerySet
from django.views.generic import DetailView
from django.views.generic import ListView
from menus.utils import set_language_changer
from parler.views import TranslatableSlugMixin

from backend.articles.models import Article
from backend.articles.models import Category


class ArticleList(AppConfigMixin, ListView):
    model = Article
    template_name = 'articles/article-list.html'

    def get_queryset(self) -> QuerySet:
        queryset_original = super().get_queryset().published()
        category = self._get_category_from_kwargs()
        is_filtered_by_category = category is not None
        if is_filtered_by_category:
            return queryset_original\
                .filter(category=category)\
                .order_by('-publication_date', '-creation_date')
        else:
            return queryset_original.order_by('-publication_date', '-creation_date')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['category_current'] = self._get_category_from_kwargs()
        context['categories'] = Category.objects.all()
        return context

    def _get_category_from_kwargs(self) -> Optional[Category]:
        category = Category.objects\
            .translated(slug=self.kwargs.get('slug'))\
            .first()
        return category


class ArticleDetail(AppConfigMixin, TranslatableSlugMixin, DetailView):
    model = Article
    template_name = 'articles/article-detail.html'

    # noinspection PyAttributeOutsideInit
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.namespace, self.config = get_app_instance(request)
        self.object = self.get_object()
        self.set_language_changer(self.object)
        return super().dispatch(request, *args, **kwargs)

    def set_language_changer(self, category):
        """Translate the slug while changing the language."""
        set_language_changer(self.request, category.get_absolute_url)

    def get_queryset(self) -> QuerySet:
        """
        Base queryset returns published Blog with respect to
        namespace.
        """
        qs = super().get_queryset()
        # if config is none - probably apphook reload is in progress, or
        # something is wrong, anyway do not fail with 500
        if self.config is None:
            return Article.objects.none()

        if self.request.user.is_staff or self.request.user.is_superuser:
            return qs.namespace(self.namespace)
        else:
            return qs.published().namespace(self.namespace)
