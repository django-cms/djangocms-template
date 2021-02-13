from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from backend.plugins.module_name import MODULE_NAME

from .models import VerticalSpacerPlugin


@plugin_pool.register_plugin
class SpacerPluginBase(CMSPluginBase):
    model = VerticalSpacerPlugin
    name = _("Vertical Spacing")
    module = MODULE_NAME
    render_template = 'bs4_spacer/spacer-plugin.html'
    allow_children = True
    # allows the plugin to be inserted inside a TextPlugin (ckeditor)
    text_enabled = True

    fieldsets = [
        (None, {'fields': ('smart_space',)}),
        (
            _('Advanced settings'),
            {
                'classes': ('collapse',),
                'fields': (
                    'space_xs',
                    'space_sm',
                    'space_md',
                    'space_lg',
                    'space_xl',
                ),
            },
        ),
    ]
