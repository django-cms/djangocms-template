from cms.models.pluginmodel import CMSPlugin
from django.db import models


class InlineAlignmentModel(CMSPlugin):
    ALIGNMENT_CHOICES = (
        ('left', 'left'),
        ('center', 'center'),
        ('right', 'right'),
    )

    alignment = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        default=ALIGNMENT_CHOICES[0][0],
        null=True,
        blank=True,
    )

    alignment_sm = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        null=True,
        blank=True,
    )

    alignment_md = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        null=True,
        blank=True,
    )

    alignment_lg = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        null=True,
        blank=True,
    )

    alignment_xl = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        null=True,
        blank=True,
    )

    def get_classes(self):
        values = []
        if self.alignment:
            values.append("text-{}".format(self.alignment))
        if self.alignment_sm:
            values.append("text-sm-{}".format(self.alignment_sm))
        if self.alignment_md:
            values.append("text-md-{}".format(self.alignment_md))
        if self.alignment_lg:
            values.append("text-lg-{}".format(self.alignment_lg))
        if self.alignment_xl:
            values.append("text-xl-{}".format(self.alignment_xl))
        return values

    def get_classes_string(self):
        return " ".join(self.get_classes())

    def __str__(self):
        return " .".join(self.get_classes())
