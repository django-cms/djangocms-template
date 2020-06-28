from cms.models import CMSPlugin


# class LineType(Enum):
#     BLUE = 'blue'
#     GRAY = 'gray'


class HorizontalLinePlugin(CMSPlugin):
    # type = EnumField(LineType, default=LineType.BLUE)

    def __str__(self):
        return 'Horizontal line plugin'
