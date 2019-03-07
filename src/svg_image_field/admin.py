from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import SvgImageFile

admin.site.register(SvgImageFile, FileAdmin)
