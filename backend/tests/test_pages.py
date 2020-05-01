import os

from cms.models import Page
from django.test import RequestFactory
from django.test import TestCase
from django.contrib import admin

from backend.auth.models import User


class PagesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(email='test@what.digital', password='test')
        self.factory = RequestFactory()
    
    def test_homepage(self):
        print('database', os.environ['DEFAULT_DATABASE_DSN'])
        request = self.factory.get('/')
        request.user = self.user
        request.session = {}
        for model_dict in admin.site.get_app_list(request):
            print(model_dict)
        print('round two -----------------------')
        for page in Page.objects.filter(publisher_is_draft=False):
            print(page.get_absolute_url())
