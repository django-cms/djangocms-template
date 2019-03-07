from django.conf import settings


# this is needed to make uploaded files be attached to the right file class
# without this an svg file will be added to filer as a normal File instead of a SvgImageFile
# as SvgImageFile file is loaded after Image it means that all image types valid for Image will never be
# considered for SvgImageFile

# in plugins therefore two fields need to be offered (image and svg_image).

try:
    FILER_IMAGE_MODEL = settings.FILER_IMAGE_MODEL
except AttributeError:
    FILER_IMAGE_MODEL = 'filer.Image'

settings.FILER_FILE_MODELS = (
    FILER_IMAGE_MODEL,
    'svg_image_field.SvgImageFile',
    'filer.File',
)
