# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('eim_service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitinfo',
            old_name='old_kcs',
            new_name='kcs',
        ),
        migrations.AlterField(
            model_name='kcsinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 6, 33, 28, 764515), db_column=b'create_date'),
        ),
        migrations.AlterField(
            model_name='unitinfo',
            name='unit_type',
            field=models.CharField(max_length=3, choices=[(b'SVR', b'Server'), (b'JBD', b'JBOD'), (b'SWH', b'Switch')]),
        ),
    ]
