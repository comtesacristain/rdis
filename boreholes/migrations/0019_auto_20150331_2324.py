# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0018_auto_20150311_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='classification',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='operator',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='originator',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='total_depth',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
