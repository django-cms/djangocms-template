from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.default.module_name import MODULE_NAME
from . import models


class HeroImagePlugin(CMSPluginBase):
    model = models.HeroImagePluginModel
    module = MODULE_NAME
    name = _("Hero Image")
    render_template = 'hero_image_element/plugins/hero-image.html'

    allow_children = True

plugin_pool.register_plugin(HeroImagePlugin)
