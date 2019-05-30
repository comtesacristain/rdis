# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boreholes', '0019_auto_20150331_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Originator',
            fields=[
                ('origno', models.AutoField(serialize=False, primary_key=True)),
                ('originator', models.TextField()),
            ],
            options={
                'db_table': '"a"."v_originators"',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='well',
            name='originator',
        ),
        migrations.AddField(
            model_name='well',
            name='orig',
            field=models.TextField(default=None, db_column=b'originator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='origno',
            field=models.ForeignKey(db_column=b'origno', default=None, to='boreholes.Originator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='well',
            name='total_depth',
            field=models.IntegerField(),
        ),
    ]
