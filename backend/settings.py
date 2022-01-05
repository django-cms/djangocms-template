import os
from enum import Enum
from typing import List

import dj_database_url
import environ
from django.urls import reverse_lazy
from django_storage_url import dsn_configured_storage_class
from link_all.dataclasses import LinkAllModel


################################################################################
# divio
################################################################################


env = environ.Env()  # better way to read env vars


class DjangoEnv(Enum):
    LOCAL = 'local'
    TEST = 'test'
    LIVE = 'live'
    BUILD_DOCKER = 'build_docker'


DJANGO_ENV_ENUM = DjangoEnv
DJANGO_ENV = DjangoEnv(env.str('STAGE', default='local'))


if DJANGO_ENV == DjangoEnv.LOCAL:
    CACHE_URL = 'locmem://'  # to disable a warning from aldryn-django


BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BACKEND_DIR)
os.environ['BASE_DIR'] = BASE_DIR
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

BASE_DIR: str = locals()['BASE_DIR']

# environ.Env.read_env(os.path.join(BASE_DIR, '.local-env'))  # Uncomment if you use local setup without docker
DOMAIN: str = locals().get('DOMAIN', 'localhost')
SITE_NAME: str = locals().get('SITE_NAME', 'dev testing site')


################################################################################
# django
################################################################################


WSGI_APPLICATION = 'backend.wsgi.application'


DATE_FORMAT = 'F j, Y'
USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)
# you can use this on the live environment to get the full exception stack trace in the logs
DEBUG_PROPAGATE_EXCEPTIONS = env.bool('DEBUG_PROPAGATE_EXCEPTIONS', default=False)
# this is set by Divio environment automatically
SECRET_KEY = env.str('SECRET_KEY', default="this-is-not-very-random")

ALLOWED_HOSTS = [env.str('DOMAIN', default=""),]
if DEBUG:
    ALLOWED_HOSTS = ["*",]

SITE_ID = env.int('SITE_ID', default=1)

INSTALLED_APPS = []
installed_apps_overrides = [
    # for USERNAME_FIELD = 'email', before `cms` since it has a User model
    'backend.auth',

    'backend.blog',

    'djangocms_modules',
]
INSTALLED_APPS = installed_apps_overrides + INSTALLED_APPS

INSTALLED_APPS.extend([
    ## BEWARE: any application added here will not show their models in django admin UNLESS you configure them below in the ADMIN_REORDER setting.
    
    # custom user
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cuser',  # for USERNAME_FIELD = 'email' in backend.auth

    # django
    'djangocms_admin_style',  # must be before django admin to override templates
    'django.contrib.admin',

    'aldryn_sso',  # aldryn_sso must be after django.contrib.admin so it can unregister the User/Group Admin if necessary.

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # key django CMS modules
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    'gtm',
    'solo',
    'rest_framework',
    'import_export',
    'adminsortable2',
    'admin_reorder',
    'django_extensions',
    'widget_tweaks',
    'django_countries',
    'logentry_admin',
    'djangocms_helpers',
    'djangocms_helpers.divio',  # fixes a bug in divio aldryn commands
    'djangocms_helpers.sentry_500_error_handler',

    'robots',

    # django cms

    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'aldryn_apphooks_config',
    'djangocms_blog',
        'taggit',
        'taggit_autosuggest',
        'sortedm2m',
    'djangocms_icon',
    'djangocms_text_ckeditor',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_history',
    'djangocms_file',
    'djangocms_snippet',
    'djangocms_socialshare',
    # 'djangocms_algolia',
    'djangocms_page_meta',
        'meta',
    'aldryn_forms_bs4_templates',
    'aldryn_forms',
        'aldryn_forms_recaptcha_plugin',
            'snowpenguin.django.recaptcha3',
        'absolute',
        'aldryn_forms.contrib.email_notifications',
        'emailit',
    'djangocms_redirect',
    'light_gallery',
    'link_all',

    # django-filer
    'easy_thumbnails',
    'filer',
    'mptt',

    # project

    'backend.plugins.bs4_float',
    'backend.plugins.bs4_hiding',
    'backend.plugins.bs4_inline_alignment',
    'backend.plugins.bs4_spacer',
    'backend.plugins.horizontal_line',
    
    ## BEWARE: any application added here will not show their models in django admin UNLESS you configure them below in the ADMIN_REORDER setting.
])


MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'djangocms_redirect.middleware.RedirectMiddleware',
    'link_all.middleware.RedirectExceptionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]


# Configure database using DATABASE_URL; fall back to sqlite file when no
# environment variable is available, e.g. during Docker build
DATABASE_URL = env.str('DATABASE_URL', default=f'sqlite:///{BASE_DIR}/db.sqlite')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


AUTH_USER_MODEL = 'backend_auth.User'

LOCALE_PATHS = [
    os.path.join(BACKEND_DIR, 'locale'),
]

ROOT_URLCONF = 'backend.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BACKEND_DIR, 'templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django_settings_export.settings_export',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

            ],
        },
    },
]


if DJANGO_ENV == DjangoEnv.LOCAL:
    email_backend_default = 'django.core.mail.backends.console.EmailBackend'
else:
    email_backend_default = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = env.str('EMAIL_BACKEND', default=email_backend_default)

DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', f'{SITE_NAME} <info@{DOMAIN}>')


SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
# PREPEND_WWW = True (if you want to redirect domain.com/... to www.domain.com/...
HTTP_PROTOCOL = env.str('HTTP_PROTOCOL', 'https')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BACKEND_DIR, 'static_collected/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DEFAULT_MAX_AGE = 60 * 60 * 24 * 365  # the default is 5m
WHITENOISE_MAX_AGE = STATICFILES_DEFAULT_MAX_AGE


# Media files
# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN
# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = env.str('DEFAULT_STORAGE_DSN', default='file:///data/media/?url=%2Fmedia%2F')
# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')
# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = 'backend.settings.DefaultStorageClass'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'data/media/')


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
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # otherwise admins can't access the login view
LOGIN_REDIRECT_URL = '/'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # removes frustrating validations, eg `too similar to your email`
]


GTM_CONTAINER_ID = env.str('GTM_CONTAINER_ID', 'GTM-1234')

WEBPACK_DEV_URL = env.str('WEBPACK_DEV_URL', default='http://0.0.0.0:8090')


SENTRY_DSN = env.str('SENTRY_DSN', '')

SETTINGS_EXPORT = [
    'DOMAIN',
    'SITE_NAME',
    'WEBPACK_DEV_URL',
    'DJANGO_ENV',
    'DJANGO_ENV_ENUM',
    'SENTRY_DSN',
    'LANGUAGE_CODE',
    'GTM_CONTAINER_ID',
]


HIJACK_REGISTER_ADMIN = False
HIJACK_ALLOW_GET_REQUESTS = True


ADMIN_REORDER = [
    {
        'label': 'Users',
        'app': 'auth',
        'models': [
            'backend_auth.User',
            'aldryn_sso.AldrynCloudUser',
            'auth.Group',
        ],
    },
    {
        'label': 'CMS',
        'app': 'cms',
        'models': [
            'cms.Page',
            {'model': 'filer.Folder', 'label': 'Media'},
            'djangocms_redirect.Redirect',
            {'model': 'aldryn_forms.FormSubmission', 'label': 'Dynamic forms submissions'},
        ],
    },
    {
        'label': 'Blog',
        'app': 'djangocms_blog',
    },
    {
        'label': 'System Administration',
        'app': 'cms',
        'models': [
            {'model': 'sites.Site', 'label': 'Websites'},
            {'model': 'djangocms_modules.Category', 'label': 'Plugin modules categories'},
            {'model': 'djangocms_snippet.Snippet', 'label': 'HTML snippets'},
            'admin.LogEntry',

            # removed because it doesn't work on cms 3.7.3
            # 'cms.GlobalPagePermission',
            # 'cms.PageUserGroup',
            # 'cms.PageUser',
        ],
    },
    {
        'label': 'SEO',
        'app': 'cms',
        'models': [
            {'model': 'robots.Rule', 'label': 'Access rules for robots.txt'},
            {'model': 'robots.Url', 'label': 'Urls patterns for robots.txt'},
        ],
    },
]


RECAPTCHA_PUBLIC_KEY = env.str('RECAPTCHA_PUBLIC_KEY', '6LcI2-YUAAAAALOlCkObFFtMkOYj1mhiArPyupgj')  # those are djangocms-template v3 keys that allow localhost testing
RECAPTCHA_PRIVATE_KEY = env.str('RECAPTCHA_PRIVATE_KEY', '6LcI2-YUAAAAADHRo9w9nVNtPW2tPx9MS4yqEvD6')
RECAPTCHA_SCORE_THRESHOLD = 0.85


if DEBUG:
    CACHE_MIDDLEWARE_SECONDS = 0
    # there's a bug with caching - https://github.com/what-digital/divio/issues/9
    CMS_PLACEHOLDER_CACHE = False
    CMS_PLUGIN_CACHE = False
    CMS_CACHE_DURATIONS = {
        'content': 0,
        'menus': 0,
        'permissions': 0,
    }
    CMS_PAGE_CACHE = False
else:
    one_hour = 60 * 60
    four_hours = one_hour * 4
    CACHE_MIDDLEWARE_SECONDS = four_hours
    CMS_CACHE_DURATIONS = {
        'menus': one_hour,
        'permissions': one_hour,
        'content': four_hours,
    }


DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DEFAULT_PERMISSION_CLASSES': 'rest_framework.permissions.IsAuthenticated'
}

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'

    SECURE_CONTENT_TYPE_NOSNIFF = True

    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_HTTPONLY = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# CSP settings have to be updated if some external media source is used
CSP_DEFAULT_SRC = ("*", "'self'",)
CSP_STYLE_SRC = ("*", "'self'", "'unsafe-eval'", "'unsafe-inline'", )
CSP_SCRIPT_SRC = ("*", "'self'", "'unsafe-eval'", "'unsafe-inline'", )
CSP_INCLUDE_NONCE_IN = ["script-src"]
CSP_FONT_SRC = ("*", )
CSP_IMG_SRC = (
    "*", "'self'", "https://*.divio-media.org", "https://www.google.com/", "https://www.google-analytics.com/",
    "data:"
)
CSP_MEDIA_SRC = ("*", "'self'", "https://*.divio-media.org", "data:")


################################################################################
# django-cms
################################################################################


CMS_TEMPLATES = [
    ('content-full-width.html', 'full width'),
    ('whitenoise-static-files-demo.html', 'Static File Demo'),
]

X_FRAME_OPTIONS = 'SAMEORIGIN'  # for the iframe-embedded django admin

CMS_PERMISSION = True

LANGUAGE_CODE = "en"

LANGUAGES = [
    ('en', "English"),
    ('de', "German"),
]
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
PARLER_LANGUAGES = CMS_LANGUAGES


# for divio deployment, overrides control.divio.com
MIGRATION_COMMANDS = [
    'python manage.py migrate',
    'python manage.py collectstatic --noinput',
    'python manage.py test_pages_on_real_db',
    'python manage.py clear_cache',
]


CMS_PLACEHOLDER_CONF = {
    None: {
        'excluded_plugins': [
            'FormPlugin',
            'Fieldset',
            'BooleanField',
            'EmailField',
            'FileField',
            'HiddenField',
            'PhoneField',
            'NumberField',
            'ImageField',
            'MultipleSelectField',
            'MultipleCheckboxSelectField',
            'RadioSelectField',
            'SelectField',
            'TextAreaField',
            'TextField',
            'SubmitButton',
            'CaptchaField',

            'ReCaptchaFieldPlugin',
        ],
    },
}


DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 24
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = [
    ('col', 'Column'),
    # for full width columns that have no left/right padding
    ('col p-0', 'Full-width Column'),
    ('w-100', 'Break'),
    ('', 'Empty'),
]

DJANGOCMS_GOOGLEMAP_API_KEY = env.str('DJANGOCMS_GOOGLEMAP_API_KEY', '123')

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'fontSize_sizes': (
        '0.5rem;'
        '0.6rem;'
        '0.7rem;'
        '0.8rem;'
        '0.9rem;'
        '0.95rem;'
        '1rem;'
        '1.1rem;'
        '1.2rem;'
        '1.3rem;'
        '1.4rem;'
        '1.5rem;'
        '1.6rem;'
        '2rem;'
        '2.3rem;'
        '2.5rem;'
        '3rem;'
        '4rem;'
        '5rem;'
        '6rem;'
        '7rem'
    ),
    'stylesSet': f'default:{STATIC_URL}global/ts/ckeditor-config.js',
    'contentsCss': [
        f'{WEBPACK_DEV_URL}/vendor.css' if DJANGO_ENV == DjangoEnv.LOCAL else f'{STATIC_URL}dist/vendor.css',
        f'{WEBPACK_DEV_URL}/global.css' if DJANGO_ENV == DjangoEnv.LOCAL else f'{STATIC_URL}dist/global.css',
    ],
    'config': {
        'allowedContent': True, # allows html tags
        'fillEmptyBlocks': False, # doesn't seem to be doing anything, but was part of the old config
    },
    'pasteFromWordPromptCleanup': True,
    'pasteFromWordRemoveFontStyles': True,
    'forcePasteAsPlainText': False,
}
TEXT_ADDITIONAL_TAGS = [
    'iframe',  # djangocms-text-ckeditor uses html5lib to sanitize HTML and deletes iframes
]


# for djangocms-helpers send_email
META_SITE_PROTOCOL = HTTP_PROTOCOL
META_USE_SITES = True


ALGOLIA = {
    'APPLICATION_ID': env.str('ALGOLIA_APPLICATION_ID', ''),
    'API_KEY': env.str('ALGOLIA_API_KEY', ''),
    'API_KEY_READ_ONLY': env.str('ALGOLIA_API_KEY_READ_ONLY', ''),
}
# todo: dynamically add load those vars in djangocms-algolia
HAYSTACK_CONNECTIONS = {'default': {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}}  # not used but haystack demands it on its search index collection import
ALDRYN_SEARCH_EXCLUDED_PLUGINS = [
    'SectionWithImageBackgroundPlugin',
    'TocPlugin',
    'NavBarPlugin',
    'VerticalSpacerPlugin',
    'Bootstrap4HidePlugin',
    'MailchimpPlugin',
]
ALGOLIA_SEARCH_INDEX_TEXT_LIMIT = 95_000


LINK_ALL_MODELS_ADDITIONAL = [
    LinkAllModel(app_label='djangocms_blog', model_name='Post'),
    LinkAllModel(app_label='djangocms_blog', model_name='BlogCategory'),
]
LINK_ALL_ENABLE_BUTTON_PLUGIN = True


# django-filer
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# divio.com SSO - this is only relevant if you deploy to divio.com
ALDRYN_SSO_HIDE_USER_MANAGEMENT = False
ALDRYN_SSO_LOGIN_WHITE_LIST = []  # https://docs.divio.com/en/latest/reference/addons-key/#aldryn-sso-login-white-list
ALDRYN_SSO_LOGIN_URL_PREFIX = 'divio'
SSO_DSN = env.str('SSO_DSN', default=None)

ALDRYN_SSO_ENABLE_LOCALDEV = False
if DJANGO_ENV == DjangoEnv.LOCAL:
    ALDRYN_SSO_ENABLE_LOCALDEV = True

ALDRYN_SSO_ALWAYS_REQUIRE_LOGIN = False
if DJANGO_ENV == DjangoEnv.TEST or env.bool('ALDRYN_SSO_ALWAYS_REQUIRE_LOGIN', default=False):
    # stage servers must always be protected, live servers only if env var is explicitely set
    ALDRYN_SSO_ALWAYS_REQUIRE_LOGIN = True

if ALDRYN_SSO_ALWAYS_REQUIRE_LOGIN:
    # apparently the middleware is not checking ALDRYN_SSO_ALWAYS_REQUIRE_LOGIN
    # so we have to manage this here so that live sites can be public.
    # see https://github.com/divio/aldryn-sso/blob/master/aldryn_config.py#L115
    position = MIDDLEWARE.index(
        'django.contrib.auth.middleware.AuthenticationMiddleware') + 1
    MIDDLEWARE.insert(position, 'aldryn_sso.middleware.AccessControlMiddleware')

ALDRYN_SSO_ENABLE_SSO_LOGIN = env.bool('ALDRYN_SSO_ENABLE_SSO_LOGIN', default=False)
if SSO_DSN:  # production SSO is configured, let's activate SSO
    ALDRYN_SSO_ENABLE_SSO_LOGIN = True

ALDRYN_SSO_ENABLE_LOGIN_FORM = env.bool('ALDRYN_SSO_ENABLE_LOGIN_FORM', default=True)

# allow anonymous preview everywhere
# https://docs.divio.com/en/latest/reference/addons-key/#test-site-protection
SHARING_VIEW_ONLY_TOKEN_KEY_NAME = 'anonymous-access'
SHARING_VIEW_ONLY_SECRET_TOKEN = 'true'
# LOGIN_URL = 'aldryn_sso_login'
ALDRYN_SSO_ENABLE_AUTO_SSO_LOGIN = env.bool('ALDRYN_SSO_ENABLE_AUTO_SSO_LOGIN', default=True)

if ALDRYN_SSO_ENABLE_LOCALDEV:
    # because thouse routes are conditionally inserted in urls.py
    ALDRYN_SSO_LOGIN_WHITE_LIST.extend([
        reverse_lazy('aldryn_sso_localdev_login'),
        reverse_lazy('aldryn_localdev_create_user'),
    ])

ALDRYN_SSO_LOGIN_WHITE_LIST.extend([
    reverse_lazy('simple-sso-login'),
    reverse_lazy('aldryn_sso_login'),
    '/static/*',  # because we're using whitenoise, static files are delivered through django
    '/admin/*',  # for the logout route
])



if ALDRYN_SSO_ENABLE_SSO_LOGIN:
    CLOUD_USER_SESSION_EXPIRATION = 24 * 60 * 60 * 7  # 1 week

ALDRYN_SSO_OVERIDE_ADMIN_LOGIN_VIEW = ALDRYN_SSO_ENABLE_SSO_LOGIN or \
                                      ALDRYN_SSO_ENABLE_LOGIN_FORM or \
                                      ALDRYN_SSO_ENABLE_LOCALDEV

if ALDRYN_SSO_OVERIDE_ADMIN_LOGIN_VIEW:
    LOGIN_URL = 'aldryn_sso_login'
