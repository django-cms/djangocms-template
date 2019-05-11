import os
from django.utils.translation import ugettext_lazy as _


env = os.environ.get
true_values = ['1', 'true', 'y', 'yes', 'on', 1, True]


BASE_DIR = os.path.dirname(__file__)


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

MIGRATION_MODULES = {}

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
