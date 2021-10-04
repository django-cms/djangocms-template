from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path
from djangocms_helpers.sentry_500_error_handler.views import collect_500_error_user_feedback_view
from djangocms_helpers.sentry_500_error_handler.views import not_found_404_view

admin.site.enable_nav_sidebar = False

urlpatterns = [
        path('robots.txt', include('robots.urls')),
        # path('login-as-user/', include('hijack.urls', namespace='hijack')),
        path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
        path('', include('link_all.api.urls')),
        path('filer/', include('filer.urls')),
        path('admin/', admin.site.urls),
        path('', include('aldryn_sso.urls')),
    ] + i18n_patterns(
        path('', include('aldryn_sso.urls_i18n')),
        path('', include('cms.urls')),
    )

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

if not settings.DEBUG:
    handler500 = collect_500_error_user_feedback_view
    handler404 = not_found_404_view

