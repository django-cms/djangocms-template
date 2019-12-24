from cuser.admin import UserAdmin
from django.contrib import admin

from backend.auth.models import User


admin.site.register(User, UserAdmin)
