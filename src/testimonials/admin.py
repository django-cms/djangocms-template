# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from aldryn_translation_tools.admin import AllTranslationsMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin
from parler.admin import TranslatableAdmin
from aldryn_apphooks_config.admin import BaseAppHookConfig

from .models import Testimonial
from .cms_appconfig import TestimonialsConfig


class TestimonialAdmin(
    PlaceholderAdminMixin,
    AllTranslationsMixin,
    SortableAdminMixin,
    FrontendEditableAdminMixin,
    TranslatableAdmin
):
    list_display = [
        '__str__',
    ]
    # frontend_editable_fields = ()


admin.site.register(Testimonial, TestimonialAdmin)


class TestimonialsConfigAdmin(PlaceholderAdminMixin, BaseAppHookConfig):

    def get_config_fields(self):
        """
        https://github.com/aldryn/aldryn-apphooks-config
        This is required to configure the admin form at admin/testimonials/testimonialsconfig/
        """
        # this method **must** be implemented and **must** return the
        # fields defined in the above form, with the ``config`` prefix
        # This is dependent on the django-appdata API
        return ()


admin.site.register(TestimonialsConfig, TestimonialsConfigAdmin)
