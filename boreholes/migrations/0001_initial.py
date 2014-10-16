# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borehole',
            fields=[
                ('eno', models.AutoField(serialize=False, primary_key=True)),
                ('entityid', models.TextField()),
                ('entity_type', models.TextField()),
            ],
            options={
                'db_table': '"a"."entities"',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('eno', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': '"mgd"."deposits"',
            },
            bases=(models.Model,),
        ),
    ]
