from aldryn_translation_tools.models import TranslatedAutoSlugifyMixin
from aldryn_translation_tools.models import TranslationHelperMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel
from parler.models import TranslatedFields

from backend.articles.cms_appconfig import ArticlesConfig
from backend.articles.models.article import get_first_app_config


class Category(
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
    TranslatableModel,
):
    slug_source_field_name = 'name'
    
    translations = TranslatedFields(
        name=models.CharField(_('title'), max_length=255),
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
    )
    
    app_config = models.ForeignKey(
        ArticlesConfig,
        verbose_name=_('app configuration'),
        on_delete=models.PROTECT,
        default=get_first_app_config,
        null=True,
    )

    def get_absolute_url(self, language: str = None) -> str:
        from backend.articles.url_utils import get_category_url
        return get_category_url(category=self, lang_code=language)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.safe_translation_getter('name', str(self.pk))
