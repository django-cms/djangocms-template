from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import pgettext as _

from ..models import Article, ArticleListPluginModel
from .module_name import MODULE_NAME


@plugin_pool.register_plugin
class ArticleListPlugin(CMSPluginBase):
    model = ArticleListPluginModel
    name = _('plugin-name', 'Article list')
    module = MODULE_NAME
    render_template = 'articles/plugins/article-list.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        articles = Article.objects.get_queryset().namespace(instance.app_config.namespace)
        context.update({
            'articles': articles[:instance.limit.value] if instance.limit.value > 0 else articles,
        })
        return context
