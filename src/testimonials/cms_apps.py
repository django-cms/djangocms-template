# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from .cms_appconfig import TestimonialsConfig


class TestimonialsApp(CMSConfigApp):
    name = _('Testimonials')
    app_config = TestimonialsConfig
    app_name = 'testimonials'

    def get_urls(self, *args, **kwargs):
        return ['testimonials.urls']


apphook_pool.register(TestimonialsApp)
