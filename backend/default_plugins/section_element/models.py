from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum, EnumField


class MaxWidth(Enum):
    DEFAULT = '1280'
    NARROW = '960'

    class Labels:
        DEFAULT = 'default (1280px)'
        NARROW = 'narrow (960px)'


class SectionPlugin(CMSPlugin):
    name = models.CharField(max_length=2048, null=True, blank=False, default="No name", help_text="This name wont show up in the frontend, it shows on the plugin only for better orientation")
    max_width = EnumField(MaxWidth, default=MaxWidth.DEFAULT, max_length=32)


    def __str__(self):
        if self.name:
            return self.name
        return ""
