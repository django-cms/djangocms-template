# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from django.conf import settings
from aldryn_forms.cms_plugins import Field
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptcha


class ReCaptchaFieldPlugin(Field):
    name = _("ReCaptcha Field")
    render_template = True
    allow_children = False
    form_field = ReCaptchaField
    form_field_widget = ReCaptcha

    def get_form_field_widget_kwargs(self, instance):
        return {
            "public_key": settings.RECAPTCHA_PUBLIC_KEY,
        }

    form_field_enabled_options = []
    fieldset_general_fields = []
    fieldset_advanced_fields = []


plugin_pool.register_plugin(ReCaptchaFieldPlugin)
