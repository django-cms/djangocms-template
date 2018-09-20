
from __future__ import unicode_literals

from django.db.models import Q
from django.utils import timezone

from parler.managers import TranslatableQuerySet

from aldryn_apphooks_config.managers.parler import (
    AppHookConfigTranslatableManager
)


class TestimonialsQuerySet(TranslatableQuerySet):

    def active(self):
        return self.filter(is_active=True)

    def namespace(self, namespace):
        return self.filter(app_config__namespace=namespace)


class TestimonialsManager(AppHookConfigTranslatableManager):
    """
    This is used in the Testimonials model 'objects' property
    So that in views.py the queryset can be filtered more easily
    """

    def get_queryset(self):
        return TestimonialsQuerySet(self.model, using=self.db)

    def active(self):
        return self.get_queryset().active()

