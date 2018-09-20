# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='InlineAlignmentModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', auto_created=True, parent_link=True, primary_key=True, related_name='inline_alignment_plugin_inlinealignmentmodel')),
                ('alignment', models.CharField(choices=[('left', 'left'), ('center', 'center'), ('right', 'right')], default='left', max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
