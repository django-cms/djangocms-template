from typing import Optional

from aldryn_apphooks_config.managers.parler import \
    AppHookConfigTranslatableManager
from aldryn_translation_tools.models import TranslatedAutoSlugifyMixin
from aldryn_translation_tools.models import TranslationHelperMixin
from cms.models.fields import PlaceholderField
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from djangocms_redirect.models import Redirect
from filer.fields.image import FilerImageField
from parler.managers import TranslatableQuerySet
from parler.models import TranslatableModel
from parler.models import TranslatedFields

from backend.articles.cms_appconfig import ArticlesConfig


def get_first_app_config() -> Optional[ArticlesConfig]:
    if ArticlesConfig.objects.exists():
        return ArticlesConfig.objects.first().pk
    else:
        return None


class ArticleQuerySet(TranslatableQuerySet):

    def published(self):
        return self.filter(is_published=True)

    def namespace(self, namespace):
        return self.filter(app_config__namespace=namespace)


class ArticleManager(AppHookConfigTranslatableManager):
    """
    This is used in the Blog model 'objects' property
    So that in views.py the queryset can be filtered more easily
    """

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self.db)

    def published(self):
        return self.get_queryset().published()


class Article(
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
    TranslatableModel
):
    slug_source_field_name = 'title'

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        slug=models.SlugField(
            _('slug'),
            max_length=255,
            blank=True,
            unique=False,
            db_index=False,
            help_text=_(
                'Auto-generated. Used in the URL. If changed, the URL will change. '
                'Clear it to have the slug re-created.'
            ),
        ),
        teaser_description=models.TextField(_('description'), blank=True),
    )

    teaser_image = FilerImageField(on_delete=models.PROTECT, related_name='teaser_image', blank=True, null=True)

    category = models.ForeignKey('articles.Category', on_delete=models.PROTECT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
    )
    content = PlaceholderField(slotname='article_content')
    is_published = models.BooleanField(_('is published?'), default=True)
    
    publication_date = models.DateTimeField(default=timezone.now, help_text="Doesn't influence the publication time, used in sorting of the articles")
    creation_date = models.DateTimeField(auto_now_add=True)

    app_config = models.ForeignKey(
        ArticlesConfig,
        verbose_name=_('app configuration'),
        on_delete=models.PROTECT,
        default=get_first_app_config,
        null=True,
    )

    objects = ArticleManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.safe_translation_getter('title', str(self.pk))

    def get_absolute_url(self, language: str = None) -> str:
        from backend.articles.url_utils import get_article_url
        return get_article_url(article=self, lang_code=language)

    def save(self, *args, **kwargs):
        is_already_has_slug = bool(self.id)
        if is_already_has_slug:
            old = Article.objects.language(self.get_current_language()).get(pk=self.pk)
            self._update_slug_and_create_redirect_if_needed(
                old_path=old.get_absolute_url(),
                new_path=self.get_absolute_url(),
            )
        return super().save(*args, **kwargs)

    def _update_slug_and_create_redirect_if_needed(self, old_path, new_path):
        site = Site.objects.get(pk=settings.SITE_ID)
    
        if new_path != old_path and old_path and new_path:
            # set up redirect, delete old
            Redirect.objects.filter(site=site, old_path=old_path).delete()
            Redirect.objects.create(site=site, old_path=old_path, new_path=new_path)
            # update target for other existing redirects
            Redirect.objects.filter(site=site, new_path=old_path).update(new_path=new_path)
