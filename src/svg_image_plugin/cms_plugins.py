# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils.compat.dj import python_2_unicode_compatible
import re

from . import models
from cms.utils.urlutils import static_with_version




class SvgImagePlugin(CMSPluginBase):
    # form = SvgImageAdminForm
    model = models.SvgImage
    name = _("SVG Image")
    render_template = 'svg_image_plugin/plugins/svg.html'
    allow_children = False
    text_enabled = True


plugin_pool.register_plugin(SvgImagePlugin)
