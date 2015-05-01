# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0002_duplicate_deletion_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duplicate',
            old_name='deletion_status',
            new_name='action_status',
        ),
        migrations.AddField(
            model_name='duplicate',
            name='data_transferred_to',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='duplicate',
            name='deleted',
            field=models.TextField(default=b'N'),
        ),
    ]
