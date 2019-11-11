from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from backend.articles.cms_appconfig import ArticlesConfig


class ArticleTeasersCMSPlugin(CMSPlugin):
    """
    AppHookConfig aware abstract CMSPlugin class
    """
    # avoid reverse relation name clashes by not adding a related_name
    # to the parent plugin
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='+',
        parent_link=True,
        on_delete=models.CASCADE,
    )
    app_config = models.ForeignKey(
        ArticlesConfig,
        verbose_name=_('Apphook configuration'),
        on_delete=models.PROTECT,
    )

    def copy_relations(self, old_instance):
        self.app_config = old_instance.app_config
