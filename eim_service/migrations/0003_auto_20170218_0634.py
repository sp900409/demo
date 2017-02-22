# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('eim_service', '0002_auto_20170218_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kcsinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 6, 34, 46, 635459), db_column=b'create_date'),
        ),
    ]
