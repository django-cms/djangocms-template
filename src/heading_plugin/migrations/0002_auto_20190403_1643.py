# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heading_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headingplugin',
            name='text',
            field=models.TextField(default='Heading Text', null=True),
        ),
    ]