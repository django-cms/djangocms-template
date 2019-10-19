from typing import Dict
from urllib.parse import urlsplit

from django.apps.registry import Apps
from django.conf import settings
from django.db import migrations


SiteId = int


def change_default_site_name(apps: Apps, _):
    Site = apps.get_model('sites', 'Site')
    site = Site.objects.first()
    
    sites_domains: Dict[SiteId, dict] = getattr(settings, 'ALDRYN_SITES_DOMAINS', None)
    base_url = getattr(settings, 'BASE_URL', None)
    is_no_domain_config = not base_url or not sites_domains
    if is_no_domain_config:
        return
    
    if site is None:
        site = Site()

    if base_url:
        is_protocol_missing = (
            'http://' not in base_url and
            'https://' not in base_url
        )
        if is_protocol_missing:
            domain = "{0.netloc}".format(urlsplit(f'https://{base_url}'))
        else:
            domain = "{0.netloc}".format(urlsplit(base_url))
    else:
        site_id_default: SiteId = 1
        domain = sites_domains[site_id_default]['domain']

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
