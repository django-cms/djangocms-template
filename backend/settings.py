import os
import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from django.contrib.staticfiles import storage
from env_settings import env


DJANGO_ENV = env.get('DJANGO_ENV', 'dev')


################################################################################
## === django core === ##
################################################################################


MIDDLEWARE.extend([
    # django packages
    'gtm',
    'rest_framework',
    'import_export',
    'adminsortable2',
    'admin_reorder',
    'django_extensions',


    # django cms plugins
    'djangocms_icon',
    'djangocms_modules',


    # django cms packages
    'aldryn_forms_bs4_templates',
    'djangocms_redirect',

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
    
    'backend.error_handler',
])

MIDDLEWARE.extend([
    # django packages
    'admin_reorder.middleware.ModelAdminReorder',

    # django cms optional
    'djangocms_redirect.middleware.RedirectMiddleware',
])

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


LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/'),
    os.path.join(BASE_DIR, 'frontend/divio'),
]


################################################################################
## === django packages === ##
################################################################################


GTM_CONTAINER_ID = env.get('GTM_CONTAINER_ID', 'GTM-1234')


WEBPACK_DEV_URL = env.get('WEBPACK_DEV_URL', default='http://localhost:8090/assets/')


SETTINGS_EXPORT = [
    'WEBPACK_DEV_URL',
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
        environment=env.get('STAGE', 'local'),
    )


ADMIN_REORDER = [
    {
        'label': 'CMS Pages',
        'app': 'cms',
        'models': [
            'cms.Page',
            'djangocms_redirect.Redirect',
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
## === django-cms core === ##
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
## === django-cms packages === ##
################################################################################


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
    'toolbar': 'CUSTOM',
    'toolbar_CUSTOM': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles', 'FontSize'],
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
    'stylesSet': [
        {'name': 'Float Left', 'element': 'span', 'attributes': {'class': 'float-left'}},
        {'name': 'H1', 'element': 'h1'},
    ],
    'contentsCss': [
        f'{WEBPACK_DEV_URL}global.css' if env.is_dev() else f'{STATIC_URL}/dist/global.css',
        f'{WEBPACK_DEV_URL}vendor.css' if env.is_dev() else f'{STATIC_URL}/dist/vendor.css',
        f'{STATIC_URL}/djangocms_text_ckeditor/ckeditor/contents.css', # default required styles
    ],
    'config': {
        'allowedContent': True,
    }
}
