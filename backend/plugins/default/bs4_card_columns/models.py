from cms.models.pluginmodel import CMSPlugin
from django.db import models


class Bootstrap4CardColumnsModel(CMSPlugin):

    COLUMN_CHOICES = (
        ('1', '1 Column'),
        ('2', '2 Columns'),
        ('3', '3 Columns'),
        ('4', '4 Columns'),
    )

    card_columns_sm = models.CharField(
        max_length=256,
        choices=COLUMN_CHOICES,
        null=True,
        blank=True,
    )

    card_columns_md = models.CharField(
        max_length=256,
        choices=COLUMN_CHOICES,
        null=True,
        blank=True,
    )

    card_columns_lg = models.CharField(
        max_length=256,
        choices=COLUMN_CHOICES,
        null=True,
        blank=True,
    )

    card_columns_xl = models.CharField(
        max_length=256,
        choices=COLUMN_CHOICES,
        null=True,
        blank=True,
    )

    def get_classes(self):
        values = []
        if self.card_columns_sm:
            values.append("card-columns-sm-{}".format(self.card_columns_sm))
        if self.card_columns_md:
            values.append("card-columns-md-{}".format(self.card_columns_md))
        if self.card_columns_lg:
            values.append("card-columns-lg-{}".format(self.card_columns_lg))
        if self.card_columns_xl:
            values.append("card-columns-xl-{}".format(self.card_columns_xl))
        return values

    def get_classes_string(self):
        return " ".join(self.get_classes())

    def __str__(self):
        return " .".join(self.get_classes())
