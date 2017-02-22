# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RmaCase',
            fields=[
                ('no', models.AutoField(serialize=False, primary_key=True, db_column=b'No')),
                ('rma_issue_date', models.DateTimeField(null=True, db_column=b'RMA_issue_date', blank=True)),
                ('rma_number', models.CharField(unique=True, max_length=15, db_column=b'RMA_number')),
                ('rma_case_type', models.CharField(max_length=25, null=True, db_column=b'RMA_case_type', blank=True)),
                ('model', models.CharField(blank=True, max_length=10, null=True, db_column=b'Model', choices=[(b'M10', b'M10'), (b'M20', b'M20'), (b'M30', b'M30'), (b'M50', b'M50')])),
                ('serial_number', models.CharField(max_length=12, db_column=b'Serial_number')),
                ('milestone_model_name', models.CharField(max_length=25, null=True, db_column=b'Milestone_Model_Name', blank=True)),
                ('customer', models.CharField(max_length=25, null=True, db_column=b'Customer', blank=True)),
                ('customer_description', models.TextField(max_length=4000, null=True, db_column=b'Customer_description', blank=True)),
                ('factory_ship_out_date', models.DateTimeField(null=True, db_column=b'Factory_ship_out_date', blank=True)),
                ('unit_received_date', models.DateTimeField(null=True, db_column=b'Unit_received_date', blank=True)),
                ('nexcom_case_status', models.CharField(max_length=25, null=True, db_column=b'Nexcom_case_status', blank=True)),
                ('nexcom_root_cause', models.CharField(max_length=12, null=True, db_column=b'Nexcom_root_cause', blank=True)),
                ('nexcom_repair_note', models.CharField(max_length=255, null=True, db_column=b'Nexcom_repair_note', blank=True)),
                ('case_conclusion', models.CharField(max_length=25, null=True, db_column=b'Case_conclusion', blank=True)),
                ('date_of_credit', models.DateTimeField(null=True, db_column=b'Date_of_credit', blank=True)),
                ('unit_status', models.CharField(max_length=25, null=True, db_column=b'Unit_status', blank=True)),
                ('date_case_closed', models.CharField(max_length=25, null=True, db_column=b'Date_case_closed', blank=True)),
                ('original_po_field', models.CharField(max_length=25, null=True, db_column=b'Original_PO', blank=True)),
                ('arma_po_field', models.CharField(max_length=12, null=True, db_column=b'ARMA_PO', blank=True)),
                ('replacement_unit_sn', models.CharField(max_length=12, null=True, db_column=b'Replacement_Unit_S/N', blank=True)),
                ('return_s20', models.CharField(max_length=45, null=True, db_column=b'Return_S20', blank=True)),
            ],
        ),
    ]
