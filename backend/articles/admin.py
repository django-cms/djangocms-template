from aldryn_apphooks_config.admin import BaseAppHookConfig
from aldryn_translation_tools.admin import AllTranslationsMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin, \
    FrontendEditableAdminMixin
from django.contrib import admin
from parler.admin import TranslatableAdmin

from backend.articles.cms_appconfig import ArticlesConfig
from backend.articles.models import Article
from backend.articles.models import Category


@admin.register(Category)
class CategoryAdmin(
    AllTranslationsMixin,
    FrontendEditableAdminMixin,
    TranslatableAdmin,
):
    list_display = [
        '__str__',
    ]


@admin.register(Article)
class ArticleAdmin(
    PlaceholderAdminMixin,
    AllTranslationsMixin,
    FrontendEditableAdminMixin,
    TranslatableAdmin,
):
    list_display = [
        '__str__',
        'publication_date',
        'created_at',
    ]
    
    list_filter = [
        'app_config',
        'publication_date',
        'created_at',
        'author',
        'category',
    ]


@admin.register(ArticlesConfig)
class ArticlesConfigAdmin(PlaceholderAdminMixin, BaseAppHookConfig):

    def get_config_fields(self):
        """
        https://github.com/aldryn/aldryn-apphooks-config
        This is required to configure the admin form at admin/articles/articlesconfig/
        """
        # this method **must** be implemented and **must** return the
        # fields defined in the above form, with the ``config`` prefix
        # This is dependent on the django-appdata API
        return ()
