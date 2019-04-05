#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":

    # this allows django modules inside the ./src directory, without changing PYTHONPATH env variable in the environment
    BASE_DIR = os.path.dirname(__file__)
    ADDITIONAL_PYTHON_PATH = os.path.join(BASE_DIR, 'src')
    if ADDITIONAL_PYTHON_PATH not in sys.path:
        sys.path.append(ADDITIONAL_PYTHON_PATH)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
