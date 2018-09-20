# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class InlineAlignmentPlugin(CMSPluginBase):
    model = models.InlineAlignmentModel
    module = _('Layout Helpers')
    name = _("Inline Alignment")
    render_template = 'inline_alignment_plugin/plugins/inline_alignment.html'

    allow_children = True

plugin_pool.register_plugin(InlineAlignmentPlugin)
