from typing import List

from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from backend.articles.cms_appconfig import ArticlesConfig


@apphook_pool.register
class ArticlesApp(CMSConfigApp):
    name = _('Articles')
    app_config = ArticlesConfig
    app_name = 'articles'

    def get_urls(self, *args, **kwargs) -> List[str]:
        return ['backend.articles.urls.article_urls']
