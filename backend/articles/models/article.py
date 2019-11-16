from typing import Optional

from aldryn_apphooks_config.managers.parler import AppHookConfigTranslatableManager
from aldryn_translation_tools.models import TranslatedAutoSlugifyMixin
from aldryn_translation_tools.models import TranslationHelperMixin
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField
from djangocms_redirect.models import Redirect
from parler.managers import TranslatableQuerySet
from parler.models import TranslatableModel, TranslatedFields
from filer.fields.image import FilerImageField
from django.urls import reverse, NoReverseMatch

from backend.articles.cms_appconfig import ArticlesConfig
from backend.articles.cms_appconfig import DEFAULT_NAMESPACE
from backend.articles.models.category import Category


def get_first_app_config() -> Optional[ArticlesConfig]:
    if ArticlesConfig.objects.exists():
        return ArticlesConfig.objects.first().pk
    else:
        return None


def update_slug(old_path, new_path):
    """ This method compares two slugs and creates a redirect if there is a change """
    site = Site.objects.get(pk=settings.SITE_ID)

    if new_path != old_path and old_path and new_path:
        # set up redirect, delete old
        Redirect.objects.filter(site=site, old_path=old_path).delete()
        Redirect.objects.create(site=site, old_path=old_path, new_path=new_path)
        # update target for other existing redirects
        Redirect.objects.filter(site=site, new_path=old_path).update(new_path=new_path)


class ArticleQuerySet(TranslatableQuerySet):

    def active(self):
        return self.filter(is_active=True)

    def namespace(self, namespace):
        return self.filter(app_config__namespace=namespace)


class ArticleManager(AppHookConfigTranslatableManager):
    """
    This is used in the Blog model 'objects' property
    So that in views.py the queryset can be filtered more easily
    """

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self.db)

    def active(self):
        return self.get_queryset().active()


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
        description=models.TextField(_('description')),
    )

    teaser_image = FilerImageField(on_delete=models.PROTECT, related_name='teaser_image')
    background_image = FilerImageField(on_delete=models.PROTECT, related_name='background_image')

    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
    )
    content = PlaceholderField(slotname='article_content')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(_('is active?'), default=True)

    publication_date = models.DateTimeField(default=timezone.now)

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

    def get_absolute_url(self, language=None):
        """
        Returns the slug url for this item
        """
        language = language or self.get_current_language()
        slug = self.safe_translation_getter('slug', language_code=language)
        namespace = getattr(self.app_config, "namespace", DEFAULT_NAMESPACE)

        try:
            if slug:
                kwargs = {
                    'slug': slug,
                }
                with translation.override(language):
                    return reverse(
                        '{0}:article-detail'.format(namespace),
                        kwargs=kwargs,
                        current_app=namespace
                    )
        except NoReverseMatch:
            with translation.override(language):
                return reverse('{0}:article-list'.format(namespace))

    def save(self, *args, **kwargs):
        # redirect the old url to the new url permanently
        if self.id:
            # the object is edited, therefore already has a slug
            old = Article.objects.language(self.get_current_language()).get(pk=self.pk)
            update_slug(old_path=old.get_absolute_url(), new_path=self.get_absolute_url())
        return super().save(*args, **kwargs)
