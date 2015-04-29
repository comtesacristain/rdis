# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0003_auto_20150311_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('eno', models.AutoField(serialize=False, primary_key=True)),
                ('entityid', models.TextField()),
                ('entity_type', models.TextField()),
                ('confid_until', models.DateField(null=True)),
                ('access_code', models.TextField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=8311, null=True)),
            ],
            options={
                'db_table': '"a"."entities"',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='entity_type',
            new_name='purpose',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='entityid',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='well',
            name='access_code',
        ),
        migrations.RemoveField(
            model_name='well',
            name='confid_until',
        ),
        migrations.RemoveField(
            model_name='well',
            name='geom',
        ),
        migrations.AddField(
            model_name='well',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 3, 11)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='entity',
            field=models.OneToOneField(primary_key=True, default=datetime.date(2015, 3, 11), to='boreholes.Entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 3, 11)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='well_type',
            field=models.TextField(default=datetime.date(2015, 3, 11)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sample',
            name='entity',
            field=models.ForeignKey(to='boreholes.Entity', db_column=b'eno'),
        ),
        migrations.DeleteModel(
            name='Drillhole',
        ),
    ]
