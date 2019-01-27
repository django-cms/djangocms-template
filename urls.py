# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


admin.autodiscover()


def testing_500_error(request):
    """
    Testing view to generate a 500 server error
    :param request:
    :return:
    """
    raise ValueError('This is a test exception raised on purpose, for testing exception handling.')

from usermgmt.api import routers
from usermgmt.api.urls import router as usermgmt_router

# Rest Framework
router = routers.DefaultRouter()
router.extend(usermgmt_router)


urlpatterns = [
    # standard Django auth urls
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/api/', include(router.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^testing-500-error$', testing_500_error, name='testing_500_error'),
]

urlpatterns += i18n_patterns(
    url(r'^/', include('django.contrib.auth.urls')),
    # custom wrapping functionality
    url(r'^accounts/', include('usermgmt.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns


# API Example
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'url-part', AppViewSet)

# urlpatterns += [
#   url(r'^api/', include(router.urls)),
# ]
