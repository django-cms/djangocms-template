from django.template.defaultfilters import register

from backend.articles.models.article import Article
from backend.articles.models.category import Category
from backend.articles.url_utils import get_article_url as get_article_url_fn
from backend.articles.url_utils import get_category_url as get_category_url_fn


@register.simple_tag(takes_context=True)
def get_article_url(context: dict, article: Article) -> str:
    return get_article_url_fn(article, context['request'])


@register.simple_tag(takes_context=True)
def get_category_url(context: dict, category: Category) -> str:
    return get_category_url_fn(category, context['request'])
