# we'll need to refer to filer settings
from filer import settings as filer_settings
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from . import models


class SvgFilerImageField(FilerFileField):
    default_model_class = models.SvgImageFile

