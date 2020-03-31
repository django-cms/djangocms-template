from aldryn_sso.admin import AldrynCloudUserAdmin
from aldryn_sso.models import AldrynCloudUser
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CustomAldrynSsoAdmin(AldrynCloudUserAdmin):

    def linked_user(self, obj):
        html_link = '<a href="{}">{}</a>'.format(
            reverse('admin:backend_auth_user_change', args=[obj.pk]),
            obj.user,
        )
        return mark_safe(html_link)


    linked_user.short_description = _('User')
    # This can be removed once support for django < 2.0 is dropped
    linked_user.allow_tags = True
    linked_user.admin_order_field = 'user'


admin.site.unregister(AldrynCloudUser)  # https://github.com/divio/aldryn-sso/issues/45
admin.site.register(AldrynCloudUser, CustomAldrynSsoAdmin)
