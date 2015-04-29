# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0006_auto_20150311_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(primary_key=True, to='boreholes.Entity'),
        ),
    ]
