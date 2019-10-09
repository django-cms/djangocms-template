from cms.models.pluginmodel import CMSPlugin
from django.db import models
from enumfields import Enum, EnumField


class HeadingType(Enum):
    XX_SMALL = 'xxsmall' # .c-title--xxsmall
    X_SMALL = 'xsmall' # .c-title--xsmall
    SMALL = 'small' # ...
    MEDIUM = 'medium'
    STANDARD = 'standard'
    LARGE = 'large'
    XLARGE = 'xlarge'
    WITH_PLUS_ICON = 'with-plus-icon'
    WITH_PLUS_ICON_20 = 'with-plus-icon-20'
    WITH_PLUS_ICON_18 = 'with-plus-icon-18'
    WITH_TOP_LINE = 'with-top-line'
    WITH_TOP_LINE_24 = 'with-top-line-24'
    WITH_BOTTOM_LINE = 'with-bottom-line'
    BOLDER_25 = 'bolder-25'
    BOLDER_20 = 'bolder-20'

    class Labels:
        XX_SMALL = 'very very small'
        X_SMALL = 'very small'
        SMALL = 'small'
        MEDIUM = 'medium'
        STANDARD = 'standard'
        LARGE = 'large'
        XLARGE = 'very large'
        WITH_PLUS_ICON = 'with plus icon (25px)'
        WITH_PLUS_ICON_24 = 'with plus icon (20px)'
        WITH_PLUS_ICON_18 = 'with plus icon (18px)'
        WITH_TOP_LINE = 'with top line (25px)'
        WITH_TOP_LINE_24 = 'with top line (24px)'
        WITH_BOTTOM_LINE = 'with bottom line'
        BOLDER_25 = 'bolder (25px)'
        BOLDER_20 = 'bolder (20px)'

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
    text = models.TextField(null=True, blank=False, default="Heading Text")

    heading_tag = EnumField(HeadingTag, default=HeadingTag.H1, max_length=32)
    heading_type = EnumField(HeadingType, default=HeadingType.STANDARD, max_length=32)
    heading_color = EnumField(HeadingColor, default=HeadingColor.DARK, max_length=32)
    heading_alignment = EnumField(HeadingAlignment, default=HeadingAlignment.LEFT, max_length=32)



    def __str__(self):
        if self.text:
            return self.text
        return ""
