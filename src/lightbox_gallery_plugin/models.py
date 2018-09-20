from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class LightboxGalleryCmsPlugin(CMSPlugin):

    SIZE_CHOICES = (
        ('50x50', 'Small (50px)'),
        ('100x100', 'Medium (100px)'),
        ('150x150', 'Big (150px)'),
    )

    JUSTIFY_CHOICES = (
        ('justify-content-left', 'Justify left'),
        ('justify-content-center', 'Justify center'),
        ('justify-content-right', 'Justify right'),
    )

    thumbnail_size = models.CharField(
        max_length=256,
        choices=SIZE_CHOICES,
        default=SIZE_CHOICES[0][0],
        null=True,
        blank=True,
    )

    justify = models.CharField(
        max_length=256,
        choices=JUSTIFY_CHOICES,
        default=JUSTIFY_CHOICES[0][0],
        null=True,
        blank=True,
    )


class LightboxGalleryItemCmsPlugin(CMSPlugin):

    image = FilerImageField(null=True, blank=True)
    caption = models.CharField(max_length=255)

    def __str__(self):
        if self.image:
            return str(self.image)



