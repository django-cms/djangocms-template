from django.urls import path

from backend.articles.views import ArticleDetail
from backend.articles.views import ArticleList


# default view (root url) which is pointing to ^$ url
DEFAULT_VIEW = 'article-list'


urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleList.as_view(), name='category-detail'),
    path('<slug:category_slug>/<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
]
