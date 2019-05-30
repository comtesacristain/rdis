# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0013_auto_20150311_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='well',
            old_name='enddate',
            new_name='completion_date',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='startdate',
            new_name='start_date',
        ),
    ]
