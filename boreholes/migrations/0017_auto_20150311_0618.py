# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0016_auto_20150311_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='well',
            name='eno',
        ),
        migrations.AlterField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(primary_key=True, db_column=b'eno', serialize=False, to='boreholes.Entity'),
        ),
    ]
