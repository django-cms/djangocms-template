from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PageField

# django filer imports
from filer.fields.image import FilerImageField

from djangocms_text_ckeditor.fields import HTMLField
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class Bootstrap4HidePluginModel(CMSPlugin):

    hide_on_very_small_devices = models.BooleanField(
        default=False,
        help_text="hide on very small devices and upwards",
    )
    hide_on_small_devices = models.BooleanField(
        default=False,
        help_text="hide on small devices and upwards",
    )
    hide_on_medium_devices = models.BooleanField(
        default=True,
        help_text="hide on medium devices and upwards",
    )
    hide_on_large_devices = models.BooleanField(
        default=False,
        help_text="hide on large devices and upwards",
    )
    hide_on_very_large_devices = models.BooleanField(
        default=False,
        help_text="hide on very large devices",
    )

    def get_classes_string(self):
        classes = []
        if self.hide_on_very_small_devices:
            classes.append('d-none')
        else:
            classes.append('d-block')

        if self.hide_on_small_devices:
            classes.append('d-sm-none')
        else:
            classes.append('d-sm-block')

        if self.hide_on_medium_devices:
            classes.append('d-md-none')
        else:
            classes.append('d-md-block')

        if self.hide_on_large_devices:
            classes.append('d-lg-none')
        else:
            classes.append('d-lg-block')

        if self.hide_on_very_large_devices:
            classes.append('d-xl-none')
        else:
            classes.append('d-xl-block')

        return " ".join(classes)

    def __str__(self):
        val = ""
        if self.hide_on_very_large_devices:
            val += "Very Large "
        if self.hide_on_large_devices:
            val += "Large "
        if self.hide_on_medium_devices:
            val += "Medium "
        if self.hide_on_small_devices:
            val += "Small "
        if self.hide_on_very_small_devices:
            val += "Very Small "
        return val
