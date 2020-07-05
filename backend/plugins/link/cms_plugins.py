from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from backend.plugins.link.models import LinkPluginModel
from backend.plugins.module_name import MODULE_NAME


@plugin_pool.register_plugin
class LinkPlugin(CMSPluginBase):
    module = MODULE_NAME
    name = _("Link")
    model = LinkPluginModel
    render_template = 'link/link.html'
    text_enabled = True
