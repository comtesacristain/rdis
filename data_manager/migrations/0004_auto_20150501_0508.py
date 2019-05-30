# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0003_auto_20150430_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='duplicategroup',
            name='has_resolution',
            field=models.TextField(default=b'N'),
        ),
        migrations.AddField(
            model_name='duplicategroup',
            name='qaed',
            field=models.TextField(default=b'N'),
        ),
    ]
