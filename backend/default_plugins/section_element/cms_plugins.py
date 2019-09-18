from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.default_plugins.module_name import MODULE_NAME
from .models import SectionPlugin


@plugin_pool.register_plugin
class SectionPluginBase(CMSPluginBase):
    model = SectionPlugin
    module = MODULE_NAME
    name = _("Section")
    render_template = 'section_element/section-plugin.html'
    allow_children = True
