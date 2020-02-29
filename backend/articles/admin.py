from aldryn_apphooks_config.admin import BaseAppHookConfig
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from parler.admin import TranslatableAdmin

from backend.articles.cms_appconfig import ArticlesConfig
from backend.articles.models import Article
from backend.articles.models import Category


@admin.register(Category)
class CategoryAdmin(
    FrontendEditableAdminMixin,
    TranslatableAdmin,
):
    list_display = [
        '__str__',
        'app_config',
    ]


@admin.register(Article)
class ArticleAdmin(
    PlaceholderAdminMixin,
    FrontendEditableAdminMixin,
    TranslatableAdmin,
):
    list_display = [
        '__str__',
        'author',
        'category',
        'publication_date',
        'creation_date',
        'app_config',
        'is_published',
    ]

    list_filter = [
        'app_config',
        'publication_date',
        'creation_date',
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
        return 'verbose_name',
