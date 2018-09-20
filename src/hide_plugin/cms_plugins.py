# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils.compat.dj import python_2_unicode_compatible

from . import models


class Bootstrap4HidePlugin(CMSPluginBase):
    model = models.Bootstrap4HidePluginModel
    module = _('Layout Helpers')
    name = _("Hide Element")
    render_template = 'hide_plugin/plugins/hide.html'

    allow_children = True


plugin_pool.register_plugin(Bootstrap4HidePlugin)

