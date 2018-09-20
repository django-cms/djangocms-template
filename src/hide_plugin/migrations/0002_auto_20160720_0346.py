# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hide_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hidepluginmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(serialize=False, to='cms.CMSPlugin', primary_key=True, auto_created=True, parent_link=True, related_name='hide_plugin_hidepluginmodel'),
        ),
    ]
