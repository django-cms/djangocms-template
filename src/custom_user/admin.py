from django.contrib import admin
from django.contrib.auth import get_user_model
from usermgmt.admin import UserAdmin, UserValidationCodeAdmin
from usermgmt.models import UserValidationCode


admin.site.register(UserValidationCode, UserValidationCodeAdmin)
# admin.site.register(get_user_model(), UserAdmin)
