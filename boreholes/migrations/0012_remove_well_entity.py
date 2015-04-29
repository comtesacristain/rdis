# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0011_auto_20150311_0606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='well',
            name='entity',
        ),
    ]
