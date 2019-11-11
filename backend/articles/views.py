from typing import Optional

from aldryn_apphooks_config.mixins import AppConfigMixin
from django.db.models import QuerySet
from parler.views import TranslatableSlugMixin
from aldryn_apphooks_config.utils import get_app_instance
from menus.utils import set_language_changer
from django.views.generic import DetailView, ListView

from backend.articles.models import Article
from backend.articles.models import Category


class ArticleList(AppConfigMixin, ListView):
    model = Article
    template_name = 'articles/article-list.html'

    def get_queryset(self) -> QuerySet:
        queryset_original = super().get_queryset().filter(is_active=True)
        category = self._get_category_from_request()
        is_filtered_by_category = category is not None
        if is_filtered_by_category:
            return queryset_original.filter(category=category).order_by('-publication_date', '-created_at')
        else:
            return queryset_original.order_by('-publication_date', '-created_at')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['category_current'] = self._get_category_from_request()
        context['categories'] = Category.objects.all()
        return context

    def _get_category_from_request(self) -> Optional[Category]:
        category_slug = self.request.GET.get('category')
        category = Category.objects.translated(slug=category_slug).first()
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
        Base queryset returns active Blog with respect to
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
            return qs.active().namespace(self.namespace)
