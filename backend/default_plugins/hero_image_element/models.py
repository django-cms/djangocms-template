from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class HeroImagePluginModel(CMSPlugin):

    background_image = FilerImageField(on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        if self.background_image:
            return str(self.background_image)

