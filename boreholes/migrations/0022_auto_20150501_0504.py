# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0021_auto_20150428_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='confid_until',
            new_name='entrydate',
        ),
        migrations.AlterField(
            model_name='well',
            name='origno',
            field=models.ForeignKey(db_column=b'origno', to='boreholes.Originator', null=True),
        ),
    ]
