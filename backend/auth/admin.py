from django.contrib import admin
from django.contrib.admin import ModelAdmin

from backend.auth.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
    ]
    list_filter = [
        'is_active',
        'date_joined',
        'last_login',
        'is_staff',
        'is_superuser',
    ]
