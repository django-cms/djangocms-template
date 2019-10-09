from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.default.module_name import MODULE_NAME
from . import models


class LightboxGalleryPlugin(CMSPluginBase):
    model = models.LightboxGalleryCmsPlugin
    module = MODULE_NAME
    name = _("Gallery Container")
    render_template = 'bs4_lightbox_gallery/plugins/lightbox_gallery_plugin.html'
    allow_children = True
    child_classes = [
        "LightboxGalleryItemPlugin",
    ]


plugin_pool.register_plugin(LightboxGalleryPlugin)


class LightboxGalleryItemPlugin(CMSPluginBase):
    model = models.LightboxGalleryItemCmsPlugin
    module = MODULE_NAME
    name = _("Gallery Item")
    render_template = 'bs4_lightbox_gallery/plugins/lightbox_gallery_item.html'
    allow_children = False
    require_parent = True
    parent_classes = [
        "LightboxGalleryPlugin",
    ]


plugin_pool.register_plugin(LightboxGalleryItemPlugin)
