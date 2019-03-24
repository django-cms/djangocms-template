# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class HeroImagePlugin(CMSPluginBase):
    model = models.HeroImagePluginModel
    # module = _('')
    name = _("Hero Image")
    render_template = 'hero_image_plugin/plugins/hero-image.html'

    allow_children = True

plugin_pool.register_plugin(HeroImagePlugin)
