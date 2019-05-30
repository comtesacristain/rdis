# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0012_remove_well_entity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='well',
            old_name='end_date',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='start_date',
            new_name='startdate',
        ),
    ]
