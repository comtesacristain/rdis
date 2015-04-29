# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0020_auto_20150427_0358'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='well',
            table='"npm"."wells"',
        ),
    ]
