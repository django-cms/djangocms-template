# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class Bootstrap4CardColumnsPlugin(CMSPluginBase):
    model = models.Bootstrap4CardColumnsModel
    module = _('Layout Helpers')
    name = _("Card Columns")
    render_template = 'card_columns_plugin/plugins/card_columns_plugin.html'
    allow_children = True


plugin_pool.register_plugin(Bootstrap4CardColumnsPlugin)

