# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0010_well_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(primary_key=True, to='boreholes.Entity'),
        ),
    ]
