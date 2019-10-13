import os
import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from django.contrib.staticfiles import storage
from env_settings import env
# noinspection PyPackageRequirements
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env.get_or_create_secret_key(base_dir=BASE_DIR)

DJANGO_ENV_ENUM = env.DjangoEnv
DJANGO_ENV: env.DjangoEnv = env.django_env()

DEBUG: bool = env.is_debug()

ALLOWED_HOSTS = env.allowed_hosts()


INSTALLED_APPS = [
    'backend.auth', # for USERNAME_FIELD = 'email', before `cms` since it has a User model

    'djangocms_admin_style', # before `django.contrib.admin`
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # django packages
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cuser', # for USERNAME_FIELD = 'email' in backend.auth
    'parler',
    'gtm',
    'rest_framework',
    'import_export',
    'adminsortable2',
    'test_user',
    'filer',
        'easy_thumbnails',
        'mptt',
    'django_jinja',
    'lockdown',
    'admin_reorder',
    'django_extensions',

    # django cms base
    'cms',
        'menus',
        'treebeard',
        'sekizai',
        'django.contrib.sites',


    # django cms plugins
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_icon',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_history',
    'djangocms_modules',

    'aldryn_apphooks_config',
    'aldryn_translation_tools',  # not sure what it does, required by many aldryn packages
    'aldryn_forms_bs4_templates',
    'aldryn_forms',
        'captcha', # required by aldryn_forms
        'emailit', # required by aldryn_forms
        'absolute', # required by aldryn_forms, adds absolute site URL vars to context
    'aldryn_forms.contrib.email_notifications',
    
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
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

    'backend.plugins.default.bs4_float',
    'backend.plugins.default.bs4_hiding',
    'backend.plugins.default.bs4_inline_alignment',
    'backend.plugins.default.bs4_spacer',
    'backend.plugins.default.bs4_lightbox_gallery',
    'backend.plugins.default.bs4_card_columns',
    'backend.plugins.default.heading_element',
    'backend.plugins.default.hero_image_element',
    'backend.plugins.default.section_element',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'lockdown.middleware.LockdownMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    
    # django cms requirements
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    
    # django cms optional
    'cms.middleware.utils.ApphookReloadMiddleware',
]

ROOT_URLCONF = 'backend.urls'
HTTP_PROTOCOL = 'http' if env.is_dev() else 'https'
WSGI_APPLICATION = 'backend.wsgi.application'


_TEMPLATE_CONTEXT_PROCESSORS =  [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.i18n',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.media',
    'django.template.context_processors.csrf',
    'django.template.context_processors.tz',
    'django.template.context_processors.static',

    'django.contrib.messages.context_processors.messages',
    
    # django-cms requirements
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    
    # django-cms optional
    'cms.context_processors.cms_settings',
    
    # aldryn_forms requirements
    'absolute.context_processors.absolute',
    
    'django_settings_export.settings_export',
]
TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [
            'backend/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.jinja2',
            'context_processors': _TEMPLATE_CONTEXT_PROCESSORS,
        },
        'NAME': 'jinja2',
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            'backend/templates',
        ],
        'OPTIONS': {
            'context_processors': _TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

AUTH_USER_MODEL = 'backend_auth.User'


LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

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


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend'),
]


class PatchedManifestStaticFilesStorage(storage.ManifestStaticFilesStorage):
    """
    Override the replacement patterns to match URL-encoded quotations.
    We use inlined SVG data url()s that contain url_encoded quotes which dont work
    Since these css url() assets are encoded already by webpack we can completely ignore the content of css files.
    Solution from: https://code.djangoproject.com/ticket/21080#comment:12
    
    remove css from the patterns list so no css file introspection is done
    """
    patterns = ()


STATICFILES_STORAGE = 'backend.settings.PatchedManifestStaticFilesStorage'


EMAIL_BACKEND = env.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = env.get('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER', '')
EMAIL_PORT = env.get('EMAIL_PORT', '')
EMAIL_USE_TLS = env.get('EMAIL_USE_TLS', False)


BUSINESS_NAME = env.get('BUSINESS_NAME', 'backend')
BASE_URL = env.get('BASE_URL', 'http://localhost:8000')
BUSINESS_EMAIL = env.get('BUSINESS_EMAIL', 'tech@what.digital')
BUSINESS_EMAIL_VANE = '%(name)s <%(address)s>' % {
    'name': BUSINESS_NAME,
    'address': BUSINESS_EMAIL,
}
DEFAULT_FROM_EMAIL = BUSINESS_EMAIL_VANE


if env.get('DB_ENGINE') == 'django.db.backends.postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env.get('DB_NAME', 'db'),
            'USER': env.get('DB_USER', 'db'),
            'PASSWORD': env.get('DB_PASSWORD', 'db'),
            'HOST': env.get('DB_HOST', 'localhost'),
            'PORT': env.get('DB_PORT', '5432'),
        },
    }
else:
    # noinspection PyUnresolvedReferences
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }



################################################################################
# django-cms
################################################################################


CMS_TEMPLATES = [
    ('default.html', 'default template'),
]

SITE_ID = 1

CMS_LANGUAGES = {
    SITE_ID: [
        {
            'code': 'en',
            'name': 'English',
        },
        {
            'code': 'de',
            'name': 'German',
        },
    ],
    'default': {
        'fallbacks': ['en', 'de'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    }
}


################################################################################
# django packages
################################################################################


GTM_CONTAINER_ID = env.get('GTM_CONTAINER_ID', 'GTM-1234')


WEBPACK_DEV_BUNDLE = env.get('WEBPACK_DEV_BUNDLE')
WEBPACK_DEV_BUNDLE_BASE_URL = env.get(
    'WEBPACK_DEV_BUNDLE_BASE_URL',
    default='http://localhost:8090/assets/',
)


SETTINGS_EXPORT = [
    'WEBPACK_DEV_BUNDLE_BASE_URL',
    'WEBPACK_DEV_BUNDLE',
    'DJANGO_ENV',
    'DJANGO_ENV_ENUM',
    'BUSINESS_NAME',
    'SENTRY_IS_ENABLED',
    'SENTRY_DSN',
]


SENTRY_IS_ENABLED = env.get_bool('SENTRY_IS_ENABLED', False)
SENTRY_DSN = env.get('SENTRY_DSN')
if SENTRY_IS_ENABLED:
    # noinspection PyTypeChecker
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(
                level=logging.INFO,  # Capture info and above as breadcrumbs
                event_level=None,  # Send no events from log messages
            )
        ],
        environment=DJANGO_ENV.value,
    )

# noinspection PyUnresolvedReferences
file_log = env.get('LOGFILE', os.path.join(BASE_DIR, 'default.log'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            # https://docs.python.org/3/library/logging.handlers.html
            # because of https://justinmontgomery.com/rotating-logs-with-multiple-workers-in-django
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': file_log,
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


TEST_USER_USERNAME_AND_PASS = 'test@what.digital'


LOCKDOWN_ENABLED = env.get_bool('LOCKDOWN_ENABLED', False)
LOCKDOWN_FORM = 'lockdown.forms.AuthForm'
LOCKDOWN_REMOTE_ADDR_EXCEPTIONS = [
    '127.0.0.1',
    '::1',
]


# allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = HTTP_PROTOCOL
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
LOGIN_REDIRECT_URL = '/'


ADMIN_REORDER = [
    {
        'label': 'CMS Pages',
        'app': 'cms',
        'models': [
            'cms.Page',
            'cms.PageType',
            {'model': 'cms.StaticPlaceholder', 'label': 'Page static placeholders'},
        ],
    },
    {
        'label': 'CMS Plugins',
        'app': 'cms',
        'models': [
            {'model': 'aldryn_forms.FormSubmission', 'label': 'Dynamic forms submissions'},
            {'model': 'djangocms_modules.Category', 'label': 'Plugin modules categories'},
            {'model': 'djangocms_snippet.Snippet', 'label': 'HTML snippets'},
        ],
    },
    {
        'label': 'Files',
        'app': 'filer',
        'models': [
            'filer.Folder',
            {'model': 'filer.ThumbnailOption', 'label': 'Images thumbnail options'},
        ],
    },
    {
        'label': 'Users',
        'app': 'auth',
        'models': [
            'backend_auth.User',
            'auth.Group',
        ],
    },
]


################################################################################
# django-cms plugins
################################################################################


THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = [
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
]


DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 24
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = [
    ('col', 'Column'),
    # for full width columns that have no left/right padding
    ('col p-0', 'Full-width Column'),
    ('w-100', 'Break'),
    ('', 'Empty'),
]

# djangocms-maps
MAPS_PROVIDERS = [
    ('mapbox', 'Mapbox OSM (API key required)'),
]
MAPS_MAPBOX_API_KEY = env.get('MAPS_MAPBOX_API_KEY', '123')


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
    'stylesSet': 'default:{}/js/ckeditor.wysiwyg.js'.format(STATIC_URL),
    # NOTE: cms plugins don't work in 'HtmlField', at all!
    # see https://github.com/divio/djangocms-text-ckeditor/issues/317
    # This is needed so that in the TextPlugin, the real styles are showing, for example for normal text and headings

    'contentsCss': [
        '{}/dist/vendor.css'.format(STATIC_URL) if WEBPACK_DEV_BUNDLE 
            else '{}/vendor.css'.format(WEBPACK_DEV_BUNDLE_BASE_URL),
        '{}/dist/app.css'.format(STATIC_URL) if WEBPACK_DEV_BUNDLE
            else '{}/app.css'.format(WEBPACK_DEV_BUNDLE_BASE_URL),
        # default styles, this is important to keep some basic styling in the ckeditor modal, such as modal paddings
        '{}/djangocms_text_ckeditor/ckeditor/contents.css'.format(STATIC_URL),
    ]
}
