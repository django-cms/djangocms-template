from cms.models.pluginmodel import CMSPlugin
from django.db import models


class VerticalSpacerPlugin(CMSPlugin):
    smart_space = models.PositiveIntegerField(
        "Default Space",
        default=0,
        help_text="in px, for desktop, height on other devices is calculated automatically",
    )

    space_xs = models.PositiveIntegerField(
        "All screens (default value)",
        default=0,
        help_text="in px for extra small screens and above",
        blank=True,
        null=True,
    )
    space_sm = models.PositiveIntegerField(
        "small screens and above",
        help_text="in px for small screens and above",
        blank=True,
        null=True,
    )
    space_md = models.PositiveIntegerField(
        "medium screens and above",
        help_text="in px for medium screens and above",
        blank=True,
        null=True,
    )
    space_lg = models.PositiveIntegerField(
        "large screens and above",
        help_text="in px for large screens and above",
        blank=True,
        null=True,
    )
    space_xl = models.PositiveIntegerField(
        "very large screens", help_text="in px for extra large screens", blank=True, null=True
    )

    def has_advanced_settings(self):
        # 0 doesnt count
        return self.space_xs or self.space_sm or self.space_md or self.space_lg or self.space_xl

    def __str__(self):
        return "smart {}, xs {}, sm {}, md {}, lg {}, xl {}".format(
            self.smart_space,
            self.space_xs,
            self.space_sm,
            self.space_md,
            self.space_lg,
            self.space_xl,
        )
