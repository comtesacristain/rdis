# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duplicate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eno', models.IntegerField(null=True)),
                ('table_name', models.TextField(null=True)),
                ('entity_type', models.TextField(null=True)),
                ('entityid', models.TextField(null=True)),
                ('x', models.FloatField(null=True)),
                ('y', models.FloatField(null=True)),
                ('z', models.FloatField(null=True)),
                ('has_well', models.BooleanField(default=False)),
                ('has_samples', models.BooleanField(default=False)),
                ('no_samples', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DuplicateGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.TextField(null=True)),
                ('field', models.TextField(null=True)),
                ('num_dupes', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='duplicate',
            name='duplicate_group',
            field=models.ForeignKey(to='data_manager.DuplicateGroup', null=True),
            preserve_default=True,
        ),
    ]
