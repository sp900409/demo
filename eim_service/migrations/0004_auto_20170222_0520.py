# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('eim_service', '0003_auto_20170218_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='kcsinfo',
            name='kcs_type',
            field=models.CharField(default=b'OLD', max_length=5, choices=[(b'OLD', b'KCS for old system'), (b'NEW', b'KCS for new system'), (b'DST', b'Destory')]),
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 5, 20, 0, 959788), db_column=b'create_date'),
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='receive_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='ship_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
