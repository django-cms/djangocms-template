from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum, EnumField


class HeadingTag(Enum):
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    H6 = 'h6'
    DIV = 'div'
    P = 'p'


class HeadingColor(Enum):
    # dark doesnt have any styles, it's just the default title, but we give a value anyway
    DARK = 'dark'  # .c-title
    WHITE = 'white' # .c-title--color-white
    BLUE = 'blue' # .c-title--color-blue


class HeadingAlignment(Enum):
    LEFT = 'left' # .text-left
    CENTER = 'center' # .text-center
    RIGHT = 'right' # ...


class HeadingPlugin(CMSPlugin):
    text = models.CharField(max_length=4096)
    heading_tag = EnumField(HeadingTag, default=HeadingTag.H1, max_length=32)
    heading_color = EnumField(HeadingColor, default=HeadingColor.DARK, max_length=32)
    heading_alignment = EnumField(HeadingAlignment, default=HeadingAlignment.LEFT, max_length=32)

    def __str__(self) -> str:
        if self.text:
            return self.text
        return ""
