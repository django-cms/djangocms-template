from cms.models import Page
from django.core.management import call_command
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase
from django.contrib import admin
from django.urls import reverse
from django.apps import apps

from backend.auth.models import User


class PagesTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user = User.objects.create_superuser(email='test@what.digital', password='test')
        cls.client = Client()
        cls.client.force_login(user)

        factory = RequestFactory()
        request = factory.get('/')
        request.user = user
        request.session = {}
        cls.request = request

        call_command('migrate')

    def test_admin_and_public_pages(self):
        for model_config_dict in admin.site.get_app_list(self.request):
            app_label: str = model_config_dict['app_label']
            for model_dict in model_config_dict['models']:
                model_name: str = model_dict['object_name']
                model_first_instance = apps.get_model(app_label, model_name)
                if model_first_instance:
                    change_url = reverse(
                        f'admin:{app_label}_{model_name.lower()}_change',
                        args=[model_first_instance.pk],
                    )
                    self._check_url_for_errors(change_url)
                    
                list_url = reverse(f'admin:{app_label}_{model_name.lower()}_changelist')
                self._check_url_for_errors(list_url)

                add_url = reverse(f'admin:{app_label}_{model_name.lower()}_add')
                self._check_url_for_errors(add_url)

        for page_published in Page.objects.filter(publisher_is_draft=False):
            self._check_url_for_errors(page_published.get_absolute_url())

    def _check_url_for_errors(self, url):
        response = self.client.get(url)
        self.assertTrue(response.status_code < 500)
