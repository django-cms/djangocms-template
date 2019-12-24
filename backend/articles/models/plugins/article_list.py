from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import pgettext as _
from enumfields import Enum, EnumField

from ...models import get_first_app_config
from ...cms_appconfig import ArticlesConfig


class Limit(Enum):
    ALL = 0
    THREE = 3
    SIX = 6
    NINE = 9

    class Labels:
        ALL = 'All articles'
        THREE = '3 articles'
        SIX = '6 articles'
        NINE = '9 articles'


class ArticleListPluginModel(CMSPlugin):
    limit = EnumField(
        Limit,
        verbose_name=_('verbose-name', 'Articles limit'),
        help_text=_('help-text', 'Optional'),
        default=Limit.ALL,
    )
    app_config = models.ForeignKey(
        ArticlesConfig,
        verbose_name=_('verbose-name', 'App configuration'),
        on_delete=models.PROTECT,
        default=get_first_app_config
    )
