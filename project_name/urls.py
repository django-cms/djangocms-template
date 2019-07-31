from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.views.static import serve


from project_name import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^', include('cms.urls')),
]

if settings.env.is_dev():
    urlpatterns = urlpatterns + staticfiles_urlpatterns() + [
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True,
            },
        ),
    ]
