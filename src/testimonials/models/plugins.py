# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..cms_appconfig import TestimonialsConfig


class TestimonialsTeaserCMSPlugin(CMSPlugin):
    """
    AppHookConfig aware abstract CMSPlugin class
    """
    # avoid reverse relation name clashes by not adding a related_name
    # to the parent plugin
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)
    app_config = models.ForeignKey(TestimonialsConfig, verbose_name=_('Apphook configuration'))

    def copy_relations(self, old_instance):
        self.app_config = old_instance.app_config

