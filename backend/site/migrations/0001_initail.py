from urllib.parse import urlsplit

from django.apps.registry import Apps
from django.conf import settings
from django.db import migrations


def change_default_site_name(apps: Apps, _):
    Site = apps.get_model('sites', 'Site')
    site = Site.objects.first()
    
    if settings.BASE_URL is None:
        return

    is_protocol_missing = (
        'http://' not in settings.BASE_URL and
        'https://' not in settings.BASE_URL
    )
    if is_protocol_missing:
        domain = "{0.netloc}".format(urlsplit(f'https://{settings.BASE_URL}'))
    else:
        domain = "{0.netloc}".format(urlsplit(settings.BASE_URL))

    site.domain = domain
    site.name = domain
    site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(change_default_site_name),
    ]
