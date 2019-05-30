# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0017_auto_20150311_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='well',
            old_name='well_type',
            new_name='welltype',
        ),
    ]
