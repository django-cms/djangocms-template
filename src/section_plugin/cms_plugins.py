from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import SectionPlugin


@plugin_pool.register_plugin
class SectionPluginBase(CMSPluginBase):
    model = SectionPlugin
    # module = _('')
    name = _("Section Plugin")
    render_template = 'section_plugin/section-plugin.html'
    allow_children = True
