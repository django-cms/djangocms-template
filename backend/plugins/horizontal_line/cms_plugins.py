from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import pgettext as _

from backend.plugins.horizontal_line.models import HorizontalLinePlugin
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class HorizontalLinePluginBase(CMSPluginBase):
    module = MODULE_NAME
    model = HorizontalLinePlugin
    name = _('field-name', 'Horizontal line')
    render_template = 'horizontal_line/horizontal-line-plugin.html'
    text_enabled = True
