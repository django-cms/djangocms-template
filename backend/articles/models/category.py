from aldryn_translation_tools.models import TranslatedAutoSlugifyMixin, \
    TranslationHelperMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatedFields, TranslatableModel


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
                'Auto-generated. Used in the URL. If changed, the URL will change. Clear it to have the slug re-created.'
            ),
        ),
    )

    def __str__(self) -> str:
        return self.safe_translation_getter('name', str(self.pk))
