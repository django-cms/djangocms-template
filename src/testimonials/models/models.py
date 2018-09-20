# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from aldryn_translation_tools.models import (
    TranslationHelperMixin, TranslatedAutoSlugifyMixin,
)
from cms.models.fields import PlaceholderField
from parler.models import TranslatableModel, TranslatedFields
from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse, NoReverseMatch
from ..cms_appconfig import TestimonialsConfig
from ..managers import TestimonialsManager


def get_first_app_config():
    if TestimonialsConfig.objects.exists():
        return TestimonialsConfig.objects.first().pk


class Testimonial(
    TranslatedAutoSlugifyMixin,
    TranslationHelperMixin,
    TranslatableModel
):
    slug_source_field_name = 'title'

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        slug=models.SlugField(
            _('slug'), max_length=255, blank=True,
            unique=False, db_index=False,
            help_text=_(
                'Auto-generated. Used in the URL. If changed, the URL will change. Clear it to have the slug re-created.'
            )),
        summary=models.CharField(_('summary'), max_length=2048),
    )

    content = PlaceholderField(slotname='testimonial_content')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(_('active?'), default=True)
    ordering = models.IntegerField(_('ordering'), default=0)
    thumbnail = FilerImageField(null=True, blank=True, related_name="thumbnail_testimonial")

    app_config = models.ForeignKey(
        TestimonialsConfig, null=True,
        verbose_name=_('app configuration'),
        on_delete=models.PROTECT,
        default=get_first_app_config,
    )

    objects = TestimonialsManager()

    class Meta:
        app_label = 'testimonials'
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
        ordering = ['ordering', ]

    def __str__(self):
        return self.safe_translation_getter('title', str(self.pk))

    def get_absolute_url(self, language=None):
        """
        Returns the slug url for this item
        """
        language = language or self.get_current_language()
        slug = self.safe_translation_getter('slug', language_code=language)
        namespace = getattr(self.app_config, "namespace", "testimonials")

        try:
            if slug:
                kwargs = {
                    'slug': slug,
                }
                return reverse(
                    '{0}:testimonials-detail'.format(namespace),
                    kwargs=kwargs,
                    current_app=namespace
                )
        except NoReverseMatch:
            return reverse('{0}:testimonials-list'.format(namespace))
