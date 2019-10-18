from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
