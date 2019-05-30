# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0014_auto_20150311_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(primary_key=True, default=0, to='boreholes.Entity'),
            preserve_default=True,
        ),
    ]
