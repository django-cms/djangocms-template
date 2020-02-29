from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .module_name import MODULE_NAME
from ..models import ArticleLinkModel


@plugin_pool.register_plugin
class ArticleLinkPlugin(CMSPluginBase):
    model = ArticleLinkModel
    module = MODULE_NAME
    name = _('Article link')
    render_template = 'articles/plugins/link-plugin.html'
    allow_children = False
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
