# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
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
            name='Sample',
            fields=[
                ('sampleno', models.AutoField(serialize=False, primary_key=True)),
                ('sampleid', models.TextField()),
                ('entity', models.ForeignKey(to='boreholes.Borehole', db_column=b'eno')),
            ],
            options={
                'db_table': '"a"."samples"',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('datano', models.AutoField(serialize=False, primary_key=True)),
                ('sample', models.ForeignKey(to='boreholes.Sample', db_column=b'sampleno')),
            ],
            options={
                'db_table': '"a"."sampledata"',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
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
        migrations.AddField(
            model_name='borehole',
            name='access_code',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='borehole',
            name='confid_until',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='borehole',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=8311, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposit',
            name='access_code',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposit',
            name='confid_until',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposit',
            name='entity_type',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposit',
            name='entityid',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposit',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=8311, null=True),
            preserve_default=True,
        ),
    ]
