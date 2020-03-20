from cuser.admin import UserAdmin
from django.contrib import admin
from hijack_admin.admin import HijackUserAdminMixin

from backend.auth.models import User


class CustomUserAdmin(UserAdmin, HijackUserAdminMixin):
    pass


admin.site.register(User, CustomUserAdmin)
