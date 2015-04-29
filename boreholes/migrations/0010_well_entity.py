# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0009_remove_well_entity'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(null=True, to='boreholes.Entity'),
            preserve_default=True,
        ),
    ]
