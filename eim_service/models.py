import datetime
from django.db import models

# Create your models here.

class KcsInfo(models.Model):
    KCS_TYPES_CHOICES = (
        ('OLD', 'KCS for old system'),
        ('NEW', 'KCS for new system'),
        ('DST', 'Destory'),
    )
    kcs_id = models.AutoField(primary_key=True)
    kcs_number = models.CharField(db_column='kcs_number', unique='True',
                                  max_length=20, blank=False)
    kcs_type = models.CharField(max_length=5, choices=KCS_TYPES_CHOICES, default='OLD', blank=False)

    create_date = models.DateTimeField(db_column='create_date',
                                       default=datetime.datetime.utcnow())
    receive_date = models.DateTimeField(blank=True, null=True)
    ship_date = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'kcs_info'
    def __str__(self):
        return self.kcs_number

class UnitInfo(models.Model):
    TYPES_CHOICES = (
        ('SVR', 'Server'),
        ('JBD', 'JBOD' ),
        ('SWH', 'Switch' ),
    )
    STATUS_CHOICES = (
        ('Created', 'Created'),
        ('Received', 'Received'),
        ('Testing', 'Testing'),
        ('Finished', 'Finished'),
        ('Packed', 'Packed'),
        ('Billed', 'Billed'),
    )

    unit_no = models.AutoField(primary_key=True)
    kcs = models.ForeignKey(KcsInfo)

    unit_serial_number = models.CharField(max_length=30, unique=True)
    unit_type = models.CharField(max_length=3, choices=TYPES_CHOICES)
    unit_status = models.CharField(max_length=10, default='Created',
                                   choices=STATUS_CHOICES)
    class Meta:
        managed = True
        db_table = 'unit_info'

    def __str__(self):
        return self.unit_serial_number

class testing_info():
    pass
