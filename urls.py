import aldryn_addons.urls
from aldryn_django.utils import i18n_patterns
from django.conf import settings
from django.urls import include
from djangocms_helpers.sentry_500_error_handler.views import collect_500_error_user_feedback_view

urlpatterns = [
    url(r'^robots\.txt', include('robots.urls')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns(),  # MUST be the last entry!
)


if not settings.DEBUG:
    handler500 = collect_500_error_user_feedback_view
