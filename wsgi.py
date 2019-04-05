"""
WSGI config for your project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# this allows django modules inside the ./src directory, without changing PYTHONPATH env variable in the environment
BASE_DIR = os.path.dirname(__file__)
ADDITIONAL_PYTHON_PATH = os.path.join(BASE_DIR, 'src')
if ADDITIONAL_PYTHON_PATH not in sys.path:
    sys.path.append(ADDITIONAL_PYTHON_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
