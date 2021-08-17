from cuser.admin import UserAdmin
from django.contrib import admin
# from hijack_admin.admin import HijackUserAdminMixin

from backend.auth.models import User


# TODO: fully install the hijacking functionality
#    see here: https://django-hijack.readthedocs.io/en/stable/#after-installing
# class CustomUserAdmin(UserAdmin, HijackUserAdminMixin):
#    pass


admin.site.register(User, UserAdmin)
