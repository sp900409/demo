# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KcsInfo',
            fields=[
                ('kcs_id', models.AutoField(serialize=False, primary_key=True)),
                ('kcs_number', models.CharField(unique=b'True', max_length=20, db_column=b'kcs_number')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2017, 2, 18, 6, 21, 23, 24924), db_column=b'create_date')),
                ('receive_date', models.DateTimeField(null=True, blank=True)),
                ('ship_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'kcs_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnitInfo',
            fields=[
                ('unit_no', models.AutoField(serialize=False, primary_key=True)),
                ('unit_serial_number', models.CharField(unique=True, max_length=30)),
                ('unit_type', models.CharField(max_length=3, choices=[(b'Server', b'SVR'), (b'JBOD', b'JBD'), (b'SWH', b'SWH')])),
                ('unit_status', models.CharField(default=b'Created', max_length=10, choices=[(b'Created', b'Created'), (b'Received', b'Received'), (b'Testing', b'Testing'), (b'Finished', b'Finished'), (b'Packed', b'Packed'), (b'Billed', b'Billed')])),
                ('old_kcs', models.ForeignKey(to='eim_service.KcsInfo')),
            ],
            options={
                'db_table': 'unit_info',
                'managed': True,
            },
        ),
    ]
