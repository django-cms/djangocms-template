from django.contrib import admin
from parler.admin import TranslatableAdmin
from solo.admin import SingletonModelAdmin

from backend.site_config.models import SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(TranslatableAdmin, SingletonModelAdmin):
    pass
