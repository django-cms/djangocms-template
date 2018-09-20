# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class LightboxGalleryPlugin(CMSPluginBase):
    model = models.LightboxGalleryCmsPlugin
    module = _('Lightbox Gallery')
    name = _("Gallery Container")
    render_template = 'lightbox_gallery_plugin/plugins/lightbox_gallery_plugin.html'
    allow_children = True
    child_classes = [
        "LightboxGalleryItemPlugin",
    ]


plugin_pool.register_plugin(LightboxGalleryPlugin)


class LightboxGalleryItemPlugin(CMSPluginBase):
    model = models.LightboxGalleryItemCmsPlugin
    module = _('Lightbox Gallery')
    name = _("Gallery Item")
    render_template = 'lightbox_gallery_plugin/plugins/lightbox_gallery_item.html'
    allow_children = False
    require_parent = True
    parent_classes = [
        "LightboxGalleryPlugin",
    ]


plugin_pool.register_plugin(LightboxGalleryItemPlugin)
