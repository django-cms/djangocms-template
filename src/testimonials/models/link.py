from cms.models.pluginmodel import CMSPlugin
from django.db import models
from ..models import Testimonial

class TestimonialLinkModel(CMSPlugin):
    # and now... magic! the "name" field is automatically assumed to be the field that will hold the selected text
    name = models.CharField(max_length=2048, blank=False)
    item = models.ForeignKey(Testimonial, on_delete=models.PROTECT)
