from django.utils.translation import ugettext as _
from aldryn_apphooks_config.models import AppHookConfig
from cms.models.fields import PlaceholderField


class ArticlesConfig(AppHookConfig):
    placeholder_article_detail_content = PlaceholderField(
        'article_content',
        related_name='article_content',
    )

    class Meta:
        verbose_name = _('Articles Configuration')
        verbose_name_plural = _('Articles Configurations')
