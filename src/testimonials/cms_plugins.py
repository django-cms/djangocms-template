# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, NoReverseMatch
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from testimonials.models import TestimonialLinkModel
from . import models


def namespace_is_apphooked(namespace):
    # avoid circular import
    from .urls import DEFAULT_VIEW
    """
    Check if provided namespace has an app-hooked page.
    Returns True or False.
    """
    try:
        reverse('{0}:{1}'.format(namespace, DEFAULT_VIEW))
    except NoReverseMatch:
        return False
    return True


class NameSpaceCheckMixin(object):

    def render(self, context, instance, placeholder):
        # check if we have a valid app_config that is app hooked to a page.
        # so that we won't have a 500 error if page with that app hook
        # was deleted.
        if instance.app_config:
            namespace = instance.app_config.namespace
        else:
            namespace = ''

        if not namespace_is_apphooked(namespace):
            context['plugin_configuration_error'] = _(
                'There is an error in plugin configuration: selected '
                'config is not available. Please switch to edit mode and '
                'change plugin app_config settings to use valid config. '
                'Also note that the testimonial app should be used at least once '
                'as an apphook for that config.')

        return super().render(context, instance, placeholder)


class TestimonialsTeasersPlugin(NameSpaceCheckMixin, CMSPluginBase):
    model = models.TestimonialsTeaserCMSPlugin
    module = _('Testimonials')
    name = _("Testimonials Teasers")
    render_template = 'testimonials/plugins/testimonials_teasers.html'

    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        if instance.app_config:
            namespace = instance.app_config.namespace
        else:
            namespace = ''
        if namespace == '' or context.get('plugin_configuration_error', False):
            testimonials = models.Testimonial.objects.none()
        else:
            testimonials = models.Testimonial.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['testimonials_count'] = len(testimonials)
        return context


plugin_pool.register_plugin(TestimonialsTeasersPlugin)


@plugin_pool.register_plugin
class TestimonialLinkPlugin(CMSPluginBase):
    model = TestimonialLinkModel
    module = _('Testimonials')
    name = _('Testimonial Link')
    render_template = 'testimonials/plugins/link-plugin.html'
    allow_children = False
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
