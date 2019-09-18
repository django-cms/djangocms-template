from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.default_plugins.module_name import MODULE_NAME
from .models import HeadingPlugin


@plugin_pool.register_plugin
class HeadingPluginBase(CMSPluginBase):
    model = HeadingPlugin
    module = MODULE_NAME
    name = _("Heading (h1, h2, ...)")
    render_template = 'heading_element/heading-plugin.html'
    allow_children = True
    # allows the plugin to be inserted inside a TextPlugin (ckeditor)
    text_enabled = True
