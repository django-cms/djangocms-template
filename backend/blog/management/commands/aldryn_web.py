import os
import subprocess
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            subprocess.check_call('aldryn-django web', shell=True)
        except subprocess.CalledProcessError as exc:
            sys.exit(exc.returncode)
