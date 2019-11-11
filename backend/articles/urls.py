from django.conf.urls import url

from .views import ArticleDetail, ArticleList

# default view (root url) which is pointing to ^$ url
DEFAULT_VIEW = 'article-list'


urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='article-list'),
    url(r'^(?P<slug>\w[-_\w]*)/$', ArticleDetail.as_view(), name='article-detail'),
]
