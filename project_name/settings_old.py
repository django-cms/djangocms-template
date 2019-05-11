import os
from django.utils.translation import ugettext_lazy as _


env = os.environ.get
true_values = ['1', 'true', 'y', 'yes', 'on', 1, True]


BASE_DIR = os.path.dirname(__file__)


if env('DJANGO_SECRET_KEY'):
    SECRET_KEY = env('DJANGO_SECRET_KEY')
else:
    key_file = os.path.join(BASE_DIR, '.secret_key')
    try:
        from pathlib import Path
        SECRET_KEY = Path(key_file).read_text()
    except (ImportError, FileNotFoundError):
        print("Generating a new SECRET_KEY (just once)")
        from django.core.management.utils import get_random_secret_key
        secret_key = get_random_secret_key()
        Path(key_file).write_text(secret_key)
        SECRET_KEY = Path(key_file).read_text()

DEBUG = env('DJANGO_DEBUG', 'True').lower() in true_values

if env('DJANGO_ALLOWED_HOSTS_STRING', False):
    ALLOWED_HOSTS = str(env('DJANGO_ALLOWED_HOSTS_STRING')).strip('"').split()
elif DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", 'localhost']

WSGI_APPLICATION = 'project_name.wsgi.application'

ROOT_URLCONF = 'project_name.urls'

LANGUAGE_CODE = 'en'

TIME_ZONE = env('TIME_ZONE_IDENTIFIER', 'Europe/Zurich')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'django_settings_export.settings_export',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'aldryn_translation_tools',
    'djangocms_modules',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_snippet',
    'djangocms_video',
    'djangocms_maps',
    'djangocms_history',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'aldryn_apphooks_config',
    'adminsortable2',
    'parler',
    'gtm',
    'svg_image_field',
    'svg_image_plugin',
    'rest_framework',
    'rest_framework.authtoken',

    'import_export',

    'aldryn_forms_bs4_templates',
    # See https://github.com/aldryn/aldryn-forms for documentation
    'absolute',
    'aldryn_forms',
    'aldryn_forms.contrib.email_notifications',
    'emailit',
]


LANGUAGES = [
    ('en', gettext('en')),
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

DATE_INPUT_FORMATS = [
    '%d.%m.%Y', '%d.%m.%y',  # European
    '%Y-%m-%d',  # ISO (for native mobile datepickers)
    '%m/%d/%Y', '%m/%d/%y',  # US
    '%d %b %Y', '%d %B %Y',  # some long formats
]

TIME_INPUT_FORMATS = [
    '%H:%M',  # '14:30'
    '%H:%M:%S',  # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
]

DATE_FORMAT = 'j F Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j F Y H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j F'
SHORT_DATE_FORMAT = 'j N Y'
SHORT_DATETIME_FORMAT = 'j N Y H:i'
FIRST_DAY_OF_WEEK = 1

# email stuff
BUSINESS_NAME = env('BUSINESS_NAME', 'Project Name')
BASE_URL = env('BASE_URL', 'http://localhost:8000')
BUSINESS_EMAIL = env('BUSINESS_EMAIL', 'tech@what.digital')
BUSINESS_EMAIL_VANE = "%(name)s <%(address)s>" % {"name": BUSINESS_NAME, "address": BUSINESS_EMAIL}
DEFAULT_FROM_EMAIL = BUSINESS_EMAIL_VANE
EMAIL_BACKEND = env('EMAIL_BACKEND', 'django.core.mail.backends.dummy.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')
EMAIL_PORT = env('EMAIL_PORT', '')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', False)

HTTPS = env('HTTPS', 'false').lower() in true_values

if HTTPS:
    PROTOCOL = 'https'
else:
    PROTOCOL = 'http'

CMS_TEMPLATES = [
    ('main.html', 'Default Template'),
]

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

if env('DB_ENGINE') == 'django.db.backends.postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME', 'db'),
            'USER': env('DB_USER', 'db'),
            'PASSWORD': env('DB_PASSWORD', 'db'),
            'HOST': env("DB_HOST", 'localhost'),
            'PORT': env("DB_PORT", "5432"),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }

MIGRATION_MODULES = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

WEBPACK_DEV_BUNDLE = env('WEBPACK_DEV_BUNDLE', 'True').lower() in true_values
WEBPACK_DEV_BUNDLE_BASE_URL = env('WEBPACK_DEV_BUNDLE_BASE_URL', 'http://localhost:8090/assets/')

STATICFILES_DIRS += [os.path.join(BASE_DIR, 'static')]

SETTINGS_EXPORT = [
    'WEBPACK_DEV_BUNDLE_BASE_URL',
    'WEBPACK_DEV_BUNDLE',
    'BUSINESS_NAME',
]

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CUSTOM',
    # http://ckeditor.com/apps/ckeditor/4.4.0/samples/plugins/toolbar/toolbar.html
    'toolbar_CUSTOM': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles', 'FontSize'],
        # ['Format', 'FontSize'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord', 'RemoveFormat'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', ],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        # we dont want 'Link', this is done by the bootstrap4 link/button plugin which covers all kind of links
        ['Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'toolbarCanCollapse': False,
    # All styling-related config is outsourced to static/djangocms_text_ckeditor/js/ckeditor.wysiwyg.js
    # because of https://github.com/aldryn/aldryn-bootstrap3/issues/154
    # https://github.com/divio/django-cms-explorer/blob/908a88afa4e1d1176e267e77eb5c61e31ef0f9e5/static/js/addons/ckeditor.wysiwyg.js#L73
    'stylesSet': 'default:{}/djangocms_text_ckeditor/js/ckeditor.wysiwyg.js'.format(STATIC_URL),
    # 'extraPlugins': 'cmsplugins' // this is already included in 'TextPlugin'
    # NOTE: cms plugins don't work in 'HtmlField', at all!
    # see https://github.com/divio/djangocms-text-ckeditor/issues/317
    # This is needed so that in the TextPlugin, the real styles are showing, for example for normal text and headings

    'contentsCss': [
        '{}/dist/vendor.css'.format(STATIC_URL) if WEBPACK_DEV_BUNDLE else "{}/vendor.css".format(
            WEBPACK_DEV_BUNDLE_BASE_URL
        ),
        '{}/dist/app.css'.format(STATIC_URL) if WEBPACK_DEV_BUNDLE else "{}/app.css".format(
            WEBPACK_DEV_BUNDLE_BASE_URL
        ),
        # default styles, this is important to keep some basic styling in the ckeditor modal, such as modal paddings
        '{}/djangocms_text_ckeditor/ckeditor/contents.css'.format(STATIC_URL),
    ]
}

CMS_PLACEHOLDER_CONF = {
    None: {
        'excluded_plugins': [],
    },
    'main_content': {
        'name': gettext("Page Content"),
        'excluded_plugins': [],
    },
    'sidebar_right': {
        'name': gettext("Sidebar Right"),
        'excluded_plugins': [],
    },
    'sidebar_left': {
        'name': gettext("Sidebar Left"),
        'excluded_plugins': [],
    },
    'testimonial_content': {
        'name': gettext("Testimonial Page Content"),
        'excluded_plugins': [],
    },
    'newsblog_listing_additional_content': {
        'name': gettext("Additional Blog Listing Page Content"),
        'excluded_plugins': [],
    },

    'newsblog_article_content': {
        'name': gettext("Newsblog Article Content"),
        'excluded_plugins': [],
    },

    'newsblog_social': {
        'name': gettext("Static Blog Article Additional Content"),
        'excluded_plugins': [],
    },
}

# djangocms-bootstrap4
# we use 24 instead of the default 12
DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 24
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', _('Column')),
    # for full width columns that have no left and right paddings
    ('col p-0', _('Full-width Column')),
    ('w-100', _('Break')),
    ('', _('Empty'))
)

# djangocms-maps
MAPS_PROVIDERS = [
    ('mapbox', _('Mapbox OSM (API key required)')),
]
MAPS_MAPBOX_API_KEY = env('MAPS_MAPBOX_API_KEY', '123')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}


if not DEBUG:
    GTM_CONTAINER_ID = env('GTM_CONTAINER_ID', "GTM-1234")


from django.contrib.staticfiles import storage

class PatchedManifestStaticFilesStorage(storage.ManifestStaticFilesStorage):
    """
    Override the replacement patterns to match URL-encoded quotations.
    We use inlined SVG data url()s that contain url_encoded quotes which dont work
    Since these css url() assets are encoded already by webpack we can completely ignore the content of css files.
    Solution from: https://code.djangoproject.com/ticket/21080#comment:12
    """
    # remove css from the patterns list so no css file introspection is done
    # this is done in webpack instead
    patterns = ()


STATICFILES_STORAGE = 'settings.PatchedManifestStaticFilesStorage'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            # https://docs.python.org/3/library/logging.handlers.html
            # because of https://justinmontgomery.com/rotating-logs-with-multiple-workers-in-django
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': env('LOGFILE', os.path.join(BASE_DIR, 'default.log')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ENVIRONMENT = env('DJANGO_ENV', 'develop')
SENTRY_IS_ENABLED = env('SENTRY_IS_ENABLED', 'false').lower() in true_values


if SENTRY_IS_ENABLED:

    import sentry_sdk
    import logging
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    # noinspection PyTypeChecker
    sentry_sdk.init(
        dsn="https://123@sentry.io/123",
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(
                level=logging.INFO,  # Capture info and above as breadcrumbs
                event_level=None  # Send no events from log messages
            )
        ],
        environment=ENVIRONMENT,
    )
