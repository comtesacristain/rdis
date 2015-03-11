# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0002_auto_20150304_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drillhole',
            fields=[
                ('eno', models.AutoField(serialize=False, primary_key=True)),
                ('entityid', models.TextField()),
                ('entity_type', models.TextField()),
                ('confid_until', models.DateField(null=True)),
                ('access_code', models.TextField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=8311, null=True)),
            ],
            options={
                'abstract': False,
                'db_table': '"a"."entities"',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('eno', models.AutoField(serialize=False, primary_key=True)),
                ('entityid', models.TextField()),
                ('entity_type', models.TextField()),
                ('confid_until', models.DateField(null=True)),
                ('access_code', models.TextField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=8311, null=True)),
            ],
            options={
                'abstract': False,
                'db_table': '"a"."entities"',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='sample',
            name='entity',
            field=models.ForeignKey(to='boreholes.Drillhole', db_column=b'eno'),
        ),
        migrations.DeleteModel(
            name='Borehole',
        ),
    ]
