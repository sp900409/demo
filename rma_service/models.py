from django.db import models

class RmaCase(models.Model):
    MODELS_CHOICES = (
        ('M10', 'M10'),
        ('M20', 'M20'),
        ('M30', 'M30'),
        ('M50', 'M50'),
    )
    no = models.AutoField(db_column='No', primary_key=True)
    rma_issue_date = models.DateTimeField(db_column='RMA_issue_date', blank=True, null=True)
    rma_number = models.CharField(db_column='RMA_number', unique=True, max_length=15)
    rma_case_type = models.CharField(db_column='RMA_case_type', max_length=25, blank=True, null=True)
    model = models.CharField(db_column='Model', choices=MODELS_CHOICES, max_length=10, blank=True, null=True)
    serial_number = models.CharField(db_column='Serial_number', max_length=12)
    milestone_model_name = models.CharField(db_column='Milestone_Model_Name', max_length=25, blank=True, null=True)
    customer = models.CharField(db_column='Customer', max_length=25, blank=True, null=True)
    customer_description = models.TextField(db_column='Customer_description', max_length=4000, blank=True, null=True)
    factory_ship_out_date = models.DateTimeField(db_column='Factory_ship_out_date', blank=True, null=True)
    unit_received_date = models.DateTimeField(db_column='Unit_received_date', blank=True, null=True)
    nexcom_case_status = models.CharField(db_column='Nexcom_case_status', max_length=25, blank=True, null=True)
    nexcom_root_cause = models.CharField(db_column='Nexcom_root_cause', max_length=12, blank=True, null=True)
    nexcom_repair_note = models.CharField(db_column='Nexcom_repair_note', max_length=255, blank=True, null=True)
    case_conclusion = models.CharField(db_column='Case_conclusion', max_length=25, blank=True, null=True)
    date_of_credit = models.DateTimeField(db_column='Date_of_credit', blank=True, null=True)
    unit_status = models.CharField(db_column='Unit_status', max_length=25, blank=True, null=True)
    date_case_closed = models.CharField(db_column='Date_case_closed', max_length=25, blank=True, null=True)
    original_po_field = models.CharField(db_column='Original_PO', max_length=25, blank=True, null=True)
    arma_po_field = models.CharField(db_column='ARMA_PO', max_length=12, blank=True, null=True)
    replacement_unit_sn = models.CharField(db_column='Replacement_Unit_S/N', max_length=12, blank=True, null=True)
    return_s20 = models.CharField(db_column='Return_S20', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.rma_number+ "\t" + self.model +"\t"+ self.nexcom_case_status+"\t"+\
               self.unit_status + "\t" +self.return_s20
