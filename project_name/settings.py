import os


env = os.environ.get


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default=get_or_create_secret_key(base_dir=BASE_DIR)
)


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'djangocms_admin_style',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # django cms base
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'django.contrib.sites',
    
    # django cms plugins
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
    'djangocms_history',
    'djangocms_bootstrap4',
    'djangocms_modules',
    
    'aldryn_apphooks_config',
    'aldryn_translation_tools',  # not sure what it does, required by many aldryn packages
    'aldryn_forms_bs4_templates',
    'aldryn_forms',
    'aldryn_forms.contrib.email_notifications',
    
    # filer
    'filer',
    'easy_thumbnails',
    'mptt',
    
    # django packages
    'parler',
    'rest_framework',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # django cms
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'sekizai.context_processors.sekizai',
]


ROOT_URLCONF = 'project_name.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'project_name.templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # django cms
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
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


EMAIL_BACKEND = env('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')
EMAIL_PORT = env('EMAIL_PORT', '')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', False)



################################################################################
# django-cms
################################################################################

CMS_TEMPLATES = [
    ('default.html', 'default template'),
]

SITE_ID = 1

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': 'English',
        },
    ],
}


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
    ('mapbox', _('Mapbox OSM (API key required)')),
]
MAPS_MAPBOX_API_KEY = env('MAPS_MAPBOX_API_KEY', '123')


################################################################################
# django packages
################################################################################

WEBPACK_DEV_BUNDLE = env_bool('WEBPACK_DEV_BUNDLE')
WEBPACK_DEV_BUNDLE_BASE_URL = env('WEBPACK_DEV_BUNDLE_BASE_URL', 'http://localhost:8090/assets/')


SETTINGS_EXPORT = [
    'WEBPACK_DEV_BUNDLE_BASE_URL',
    'WEBPACK_DEV_BUNDLE',
    'BUSINESS_NAME',
]
