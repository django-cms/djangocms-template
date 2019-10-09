from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.default.module_name import MODULE_NAME
from . import models


class Bootstrap4CardColumnsPlugin(CMSPluginBase):
    model = models.Bootstrap4CardColumnsModel
    module = MODULE_NAME
    name = _("Card Columns")
    render_template = 'bs4_card_columns/plugins/card_columns_plugin.html'
    allow_children = True


plugin_pool.register_plugin(Bootstrap4CardColumnsPlugin)

