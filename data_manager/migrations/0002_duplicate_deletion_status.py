# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duplicate',
            name='deletion_status',
            field=models.TextField(default=b'UN'),
        ),
    ]
