import os
from enum import Enum
from typing import List

from dotenv import find_dotenv
from dotenv import load_dotenv
from env_settings import env

from link_all.dataclasses import LinkAllModel


load_dotenv(find_dotenv('.env-local'))


################################################################################
# divio
################################################################################


INSTALLED_ADDONS = [
    'aldryn-addons',
    'aldryn-django',
    'aldryn-django-cms',
    'django-filer',
    'aldryn-sso',
]


BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BACKEND_DIR)
ADDONS_DIR = os.path.join(BASE_DIR, 'addons')
ADDONS_DEV_DIR = os.path.join(BASE_DIR, 'addons-dev')
os.environ['BASE_DIR'] = BASE_DIR
os.environ['ADDONS_DIR'] = ADDONS_DIR
os.environ['ADDONS_DEV_DIR'] = ADDONS_DEV_DIR
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'


import aldryn_addons.settings

aldryn_addons.settings.load(locals())


INSTALLED_APPS: List[str] = locals()['INSTALLED_APPS']
MIDDLEWARE: List[str] = locals()['MIDDLEWARE']
BASE_DIR: str = locals()['BASE_DIR']
STATIC_URL: str = locals()['STATIC_URL']
TEMPLATES: List[dict] = locals()['TEMPLATES']
DEBUG: bool = locals()['DEBUG']
MIGRATION_COMMANDS: List[str] = locals()['MIGRATION_COMMANDS']
SITE_ID: int = locals()['SITE_ID']


################################################################################
# django
################################################################################


DATE_FORMAT = 'F j, Y'

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'


class DivioEnv(Enum):
    LOCAL = 'local'
    TEST = 'test'
    LIVE = 'live'


DIVIO_ENV_ENUM = DivioEnv
DIVIO_ENV = DivioEnv(env.get('STAGE', 'local'))


installed_apps_overrides = [
    # for USERNAME_FIELD = 'email', before `cms` since it has a User model
    'backend.auth',

    'backend.blog',

    'djangocms_modules',
]
INSTALLED_APPS = installed_apps_overrides + INSTALLED_APPS

INSTALLED_APPS.extend([
    # django

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cuser',  # for USERNAME_FIELD = 'email' in backend.auth
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
    'hijack_admin',
    'djangocms_helpers',
    'djangocms_helpers.sentry_500_error_handler',
        'meta',

    # django cms

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
    'djangocms_bootstrap4.contrib.bootstrap4_picture',  # place djangocms_picture
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_bootstrap4.contrib.bootstrap4_heading',
    'aldryn_apphooks_config',
    'djangocms_blog',
        'taggit',
        'taggit_autosuggest',
        'sortedm2m',
    'djangocms_icon',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_history',
    'djangocms_picture',
    'djangocms_file',
    'djangocms_snippet',
    'djangocms_socialshare',
    'djangocms_algolia',
    'djangocms_page_meta',
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

    # project

    'backend.plugins.bs4_float',
    'backend.plugins.bs4_hiding',
    'backend.plugins.bs4_inline_alignment',
    'backend.plugins.bs4_spacer',
    'backend.plugins.horizontal_line',
])

MIDDLEWARE.extend([
    # django
    'admin_reorder.middleware.ModelAdminReorder',

    # django cms optional
    'djangocms_redirect.middleware.RedirectMiddleware',
])

# removes frustrating validations, eg `too similar to your email`
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

AUTH_USER_MODEL = 'backend_auth.User'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/'),
]

default_template_engine: dict = TEMPLATES[0]
default_template_engine['DIRS'].extend([
    os.path.join(BASE_DIR, 'backend/templates/'),
])
default_template_engine['OPTIONS']['context_processors'].extend([
    'django_settings_export.settings_export',
])

if DIVIO_ENV == DivioEnv.LOCAL:
    email_backend_default = 'django.core.mail.backends.console.EmailBackend'
else:
    email_backend_default = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = env.get('EMAIL_BACKEND', default=email_backend_default)

DEFAULT_FROM_EMAIL = env.get('DEFAULT_FROM_EMAIL', 'Project Name <info@example.com>')


if DIVIO_ENV == DivioEnv.LOCAL:
    ssl_redirect_default = False
else:
    ssl_redirect_default = True

SECURE_SSL_REDIRECT = env.get_bool('SECURE_SSL_REDIRECT', default=ssl_redirect_default)


HTTP_PROTOCOL = 'http' if DIVIO_ENV == DivioEnv.LOCAL else 'https'


################################################################################
# django optional
################################################################################


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
CONFIRM_EMAIL_ON_GET = True

GTM_CONTAINER_ID = env.get('GTM_CONTAINER_ID', 'GTM-1234')

WEBPACK_DEV_URL = env.get('WEBPACK_DEV_URL', default=f'http://localhost:8090/assets/')

# the default doesn't support names hashing
STATICFILES_STORAGE = 'aldryn_django.storage.ManifestGZippedStaticFilesStorage'
# the default is 5m
STATICFILES_DEFAULT_MAX_AGE = 60 * 60 * 24 * 365

SETTINGS_EXPORT = [
    'WEBPACK_DEV_URL',
    'DIVIO_ENV',
    'DIVIO_ENV_ENUM',
    'SENTRY_DSN',
    'GTM_CONTAINER_ID',
]


SENTRY_DSN = env.get('SENTRY_DSN', None)


HIJACK_REGISTER_ADMIN = False
HIJACK_ALLOW_GET_REQUESTS = True


ADMIN_REORDER = [
    {
        'label': 'Users',
        'app': 'auth',
        'models': [
            'backend_auth.User',
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
            
            # removed because it doesn't work on cms 3.7.1
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


RECAPTCHA_PUBLIC_KEY = env.get('RECAPTCHA_PUBLIC_KEY', '6LcI2-YUAAAAALOlCkObFFtMkOYj1mhiArPyupgj')
RECAPTCHA_PRIVATE_KEY = env.get('RECAPTCHA_PRIVATE_KEY', '6LcI2-YUAAAAADHRo9w9nVNtPW2tPx9MS4yqEvD6')
RECAPTCHA_SCORE_THRESHOLD = 0.85


################################################################################
# django-cms
################################################################################


CMS_TEMPLATES = [
    ('content-full-width.html', 'full width'),
]


X_FRAME_OPTIONS = 'SAMEORIGIN'


if DEBUG:
    # there's a bug with caching - https://github.com/what-digital/divio/issues/9
    CMS_PAGE_CACHE = False
    CMS_PLACEHOLDER_CACHE = False
    CMS_PLUGIN_CACHE = False
    MENU_CACHE_DURATION = 0
    CMS_CONTENT_CACHE_DURATION = 0


################################################################################
# django-cms optional
################################################################################


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


SHARING_VIEW_ONLY_SECRET_TOKEN = 'stage-preview'


MIGRATION_COMMANDS.insert(0, 'python manage.py test_pages_on_real_db')


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

DJANGOCMS_GOOGLEMAP_API_KEY = env.get('DJANGOCMS_GOOGLEMAP_API_KEY', '123')

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'fontSize_sizes': (
        '0.5rem;'
        '0.6rem;'
        '0.7rem;'
        '0.8rem;'
        '0.9rem;'
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
        f'{WEBPACK_DEV_URL}/vendor.css' if DIVIO_ENV == DivioEnv.LOCAL else f'{STATIC_URL}/dist/vendor.css',
        f'{WEBPACK_DEV_URL}/global.css' if DIVIO_ENV == DivioEnv.LOCAL else f'{STATIC_URL}/dist/global.css',
    ],
    'config': {
        'allowedContent': True, # allows html tags
        'fillEmptyBlocks': False, # doesn't seem to be doing anything, but was part of the old config
    },
    'pasteFromWordPromptCleanup': True,
    'pasteFromWordRemoveFontStyles': True,
    'forcePasteAsPlainText': False,
}
# djangocms-text-ckeditor uses html5lib to sanitize HTML and deletes iframes
TEXT_ADDITIONAL_TAGS = [
    'iframe',
]

# for djangocms-helpers send_email
META_SITE_PROTOCOL = HTTP_PROTOCOL
META_USE_SITES = True


ALGOLIA = {
    'APPLICATION_ID': env.get('ALGOLIA_APPLICATION_ID', ''),
    'API_KEY': env.get('ALGOLIA_API_KEY', ''),
}
# not used but haystack demands it on its search index collection import
HAYSTACK_CONNECTIONS = {'default': {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}}
ALDRYN_SEARCH_EXCLUDED_PLUGINS = [
    'SectionWithImageBackgroundPlugin',
    'TocPlugin',
    'NavBarPlugin',
    'VerticalSpacerPlugin',
    'Bootstrap4HidePlugin',
    'MailchimpPlugin',
]
ALGOLIA_SEARCH_INDEX_TEXT_LIMIT = 8_000


LINK_ALL_MODELS_ADDITIONAL = [
    LinkAllModel(app_label='djangocms_blog', model_name='Post'),
    LinkAllModel(app_label='djangocms_blog', model_name='BlogCategory'),
]


WSGI_APPLICATION = 'backend.wsgi.application'
ROOT_URLCONF = 'backend.urls'
