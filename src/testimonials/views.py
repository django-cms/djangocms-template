# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from aldryn_apphooks_config.mixins import AppConfigMixin
from parler.views import TranslatableSlugMixin
from aldryn_apphooks_config.utils import get_app_instance
from .models import Testimonial
from menus.utils import set_language_changer
from django.views.generic import DetailView, ListView


class TestimonialsList(AppConfigMixin, ListView):

    model = Testimonial
    template_name = 'testimonials/testimonials_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('ordering')


class TestimonialsDetail(AppConfigMixin, TranslatableSlugMixin, DetailView):

    model = Testimonial
    # form_class =
    template_name = 'testimonials/testimonial_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.namespace, self.config = get_app_instance(request)
        self.object = self.get_object()
        self.set_language_changer(self.object)
        return super().dispatch(request, *args, **kwargs)

    def set_language_changer(self, category):
        """Translate the slug while changing the language."""
        set_language_changer(self.request, category.get_absolute_url)

    def get_queryset(self):
        """
        Base queryset returns active Testimonials with respect to
        namespace.
        """
        qs = super().get_queryset()
        # if config is none - probably apphook reload is in progress, or
        # something is wrong, anyway do not fail with 500
        if self.config is None:
            return Testimonial.objects.none()

        return qs.active().namespace(self.namespace)
