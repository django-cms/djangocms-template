from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import HeadingPlugin


@plugin_pool.register_plugin
class HeadingPluginBase(CMSPluginBase):
    model = HeadingPlugin
    module = _('ViewFinder')
    name = _("Heading (h1, h2, ...)")
    render_template = 'heading_plugin/heading-plugin.html'
    allow_children = True
    # allows the plugin to be inserted inside a TextPlugin (ckeditor)
    text_enabled = True
