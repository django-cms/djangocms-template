# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .views import TestimonialsDetail, TestimonialsList

# default view (root url) which is pointing to ^$ url
DEFAULT_VIEW = 'testimonials-list'

urlpatterns = [
    url(r'^$', TestimonialsList.as_view(), name='testimonials-list'),
    url(r'^(?P<slug>\w[-_\w]*)/$', TestimonialsDetail.as_view(), name='testimonials-detail'),
]
