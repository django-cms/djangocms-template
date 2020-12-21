from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.module_name import MODULE_NAME

from . import models


class Bootstrap4HidePlugin(CMSPluginBase):
    model = models.Bootstrap4HidePluginModel
    module = MODULE_NAME
    name = _("Hide Element")
    render_template = 'bs4_hiding/plugins/hide.html'

    allow_children = True


plugin_pool.register_plugin(Bootstrap4HidePlugin)
