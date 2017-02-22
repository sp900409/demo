# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('eim_service', '0004_auto_20170222_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kcsinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 5, 28, 53, 594687), db_column=b'create_date'),
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='receive_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='ship_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
