# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from aldryn_apphooks_config.models import AppHookConfig
from cms.models.fields import PlaceholderField


class TestimonialsConfig(AppHookConfig):
    # PHFs
    placeholder_testimonial_detail_content = PlaceholderField(
        'testimonial_content', related_name='testimonials_testimonial_content')

    class Meta:
        verbose_name = _('Testimonials Configuration')
        verbose_name_plural = _('Testimonials Configurations')
