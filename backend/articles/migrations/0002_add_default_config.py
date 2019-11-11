from django.apps.registry import Apps
from django.db import migrations

from backend.articles.cms_appconfig import ArticlesConfig
from backend.articles.cms_appconfig import DEFAULT_NAMESPACE


def change_default_config(apps: Apps, _):
    config = ArticlesConfig()
    config.namespace = DEFAULT_NAMESPACE
    config.save()



class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(change_default_config),
    ]
