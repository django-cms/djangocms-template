import aldryn_addons.urls
from aldryn_django.utils import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from djangocms_helpers.sentry_500_error_handler.views import collect_500_error_user_feedback_view
from djangocms_helpers.sentry_500_error_handler.views import not_found_404_view


admin.site.enable_nav_sidebar = False

urlpatterns = (
    [
        path('robots.txt', include('robots.urls')),
        path('login-as-user/', include('hijack.urls', namespace='hijack')),
        path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
        path('', include('link_all.api.urls')),
    ]
    + aldryn_addons.urls.patterns()
    + i18n_patterns(
        *aldryn_addons.urls.i18n_patterns(),  # MUST be the last entry!
    )
)

if not settings.DEBUG:
    handler500 = collect_500_error_user_feedback_view
    handler404 = not_found_404_view
