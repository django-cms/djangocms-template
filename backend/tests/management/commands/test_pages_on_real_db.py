import unittest

from django.core.management import BaseCommand

from backend.tests.test_pages import PagesTestCase


class Command(BaseCommand):
    def handle(self, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(PagesTestCase)
        unittest.TextTestRunner().run(suite)
