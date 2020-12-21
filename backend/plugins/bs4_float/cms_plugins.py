from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.module_name import MODULE_NAME

from . import models


class FloatPlugin(CMSPluginBase):
    model = models.FloatModel
    module = MODULE_NAME
    name = _("Float")
    render_template = 'bs4_float/plugins/float.html'
    allow_children = True


plugin_pool.register_plugin(FloatPlugin)
