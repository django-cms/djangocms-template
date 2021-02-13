from cms.models.pluginmodel import CMSPlugin
from django.db import models


class FloatModel(CMSPlugin):
    FLOAT_CHOICES = (
        ('left', 'float left'),
        ('right', 'float right'),
    )

    FLOAT_BREAKPOINT_CHOICES = (
        ('', 'very small'),
        ('sm-', 'small'),
        ('md-', 'medium'),
        ('lg-', 'large'),
        ('xl-', 'very large'),
    )

    float_direction = models.CharField(
        max_length=256,
        choices=FLOAT_CHOICES,
        default=FLOAT_CHOICES[0][0],
    )

    float_breakpoint = models.CharField(
        max_length=256,
        choices=FLOAT_BREAKPOINT_CHOICES,
        default=FLOAT_BREAKPOINT_CHOICES[0][0],
        help_text="At which bootstrap4 breakpoint should the float behaviour start, starting from smallest.",
        blank=True,
    )

    margin_top = models.PositiveIntegerField(default=0)
    margin_right = models.PositiveIntegerField(default=0)
    margin_bottom = models.PositiveIntegerField(default=0)
    margin_left = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "float-{}{}".format(
            self.float_breakpoint,
            self.float_direction,
        )
