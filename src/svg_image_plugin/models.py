# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PageField
import re
from django.core.exceptions import ValidationError

# django filer imports
from filer.fields.image import FilerImageField

from djangocms_text_ckeditor.fields import HTMLField
from cms.utils.compat.dj import python_2_unicode_compatible

# django filer imports
from filer.fields.image import FilerFileField
from svg_image_field.fields import SvgFilerImageField


@python_2_unicode_compatible
class SvgImage(CMSPlugin):
    max_width = models.PositiveSmallIntegerField(null=True, blank=True)
    max_height = models.PositiveSmallIntegerField(null=True, blank=True)

    image = SvgFilerImageField(on_delete=models.PROTECT)

    def __str__(self):
        return str(self.image)

