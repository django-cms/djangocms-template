import logging
from typing import Union

from django.contrib import messages
from django.http import HttpRequest
from django.urls import NoReverseMatch
from django.urls import reverse
from django.utils import translation
from django.utils.translation import get_language

from backend.articles.cms_appconfig import DEFAULT_NAMESPACE
from backend.articles.models.article import Article
from backend.articles.models.category import Category


logger = logging.getLogger(__name__)


def get_article_url(article: Article, request: HttpRequest = None, lang_code: str = None) -> str:
    return _get_url(
        instance=article,
        request=request,
        lang_code=lang_code,
    )


def get_category_url(category: Category, request: HttpRequest = None, lang_code: str = None) -> str:
    return _get_url(
        instance=category,
        request=request,
        lang_code=lang_code,
    )


def _get_url(
    instance: Union[Category, Article],
    context: dict = None,
    request: HttpRequest = None,
    lang_code: str = None,
) -> str:
    language: str = lang_code or instance.get_current_language() or get_language()
    instance_slug = instance.safe_translation_getter('slug', language_code=language)
    namespace = getattr(instance.app_config, 'namespace', DEFAULT_NAMESPACE)
    
    with translation.override(language):
        if type(instance) == Article:
            instance_name = 'article'
        else:
            instance_name = 'category'
            
        url_kwargs = {f'slug': instance_slug}
        if type(instance) == Article:
            category_slug = instance.category.safe_translation_getter(
                'slug', language_code=language,
            )
            url_kwargs = {**url_kwargs, 'category_slug': category_slug}

        try:
            return reverse(
                f'{namespace}:{instance_name}-detail',
                kwargs=url_kwargs,
                current_app=namespace,
            )
        except NoReverseMatch:
            is_request_provided = context is not None or request is not None
            if is_request_provided:
                if context is not None:
                    request_provided = context.get('request')
                else:
                    request_provided = request
                messages.error(request_provided, f"The {instance_name} with the slug '{instance_slug}' was not found.")
            else:
                logger.error(
                    "Article or category not found, "
                    "user not informed because you didn't provide a request argument",
                )
            
            try:
                return reverse(f'{namespace}:article-list')
            except NoReverseMatch:
                raise Exception(
                    f"Please double check that an {instance_name} apphook page "
                    f"in {language} language was created and published."
                )
