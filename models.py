# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CreditRecord(models.Model):
    rma_no = models.CharField(db_column='RMA_No', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    credit_date = models.DateTimeField(db_column='Credit_date', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    receiving_info = models.TextField(db_column='Receiving_info', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Credit_record'


class SnChangeList(models.Model):
    id = models.AutoField(db_column='ID', unique=True)  # Field name made lowercase.
    old_sn = models.CharField(db_column='old_SN', max_length=15)  # Field name made lowercase.
    old_mac1 = models.CharField(db_column='old_MAC1', unique=True, max_length=15)  # Field name made lowercase.
    old_mac2 = models.CharField(db_column='old_MAC2', max_length=15)  # Field name made lowercase.
    new_sn = models.CharField(db_column='new_SN', unique=True, max_length=15)  # Field name made lowercase.
    new_mac1 = models.CharField(db_column='new_MAC1', max_length=15)  # Field name made lowercase.
    new_mac2 = models.CharField(db_column='new_MAC2', max_length=15)  # Field name made lowercase.
    time_changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'SN_change_list'
        unique_together = (('id', 'new_sn'),)


class SnToPo(models.Model):
    sn_to_po_id = models.AutoField(db_column='SN_to_PO_id', primary_key=True)  # Field name made lowercase.
    system_sn_field = models.CharField(db_column='System_SN#', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    milestone_po_field = models.CharField(db_column='Milestone_PO#', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'SN_to_PO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DefineList(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=45, blank=True, null=True)  # Field name made lowercase.
    options = models.CharField(db_column='Options', max_length=45, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'define_list'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NusData(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    rma_issue_date = models.DateTimeField(db_column='RMA_issue_date', blank=True, null=True)  # Field name made lowercase.
    rma_number = models.CharField(db_column='RMA_number', unique=True, max_length=15)  # Field name made lowercase.
    rma_case_type = models.CharField(db_column='RMA_case_type', max_length=25, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=5, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_number', max_length=12)  # Field name made lowercase.
    milestone_model_name = models.CharField(db_column='Milestone_Model_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=25, blank=True, null=True)  # Field name made lowercase.
    customer_description = models.CharField(db_column='Customer_description', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    factory_ship_out_date = models.DateTimeField(db_column='Factory_ship_out_date', blank=True, null=True)  # Field name made lowercase.
    unit_received_date = models.DateTimeField(db_column='Unit_received_date', blank=True, null=True)  # Field name made lowercase.
    nexcom_case_status = models.CharField(db_column='Nexcom_case_status', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nexcom_root_cause = models.CharField(db_column='Nexcom_root_cause', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nexcom_repair_note = models.CharField(db_column='Nexcom_repair_note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    case_conclusion = models.CharField(db_column='Case_conclusion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    date_of_credit = models.DateTimeField(db_column='Date_of_credit', blank=True, null=True)  # Field name made lowercase.
    unit_status = models.CharField(db_column='Unit_status', max_length=25, blank=True, null=True)  # Field name made lowercase.
    date_case_closed = models.CharField(db_column='Date_case_closed', max_length=25, blank=True, null=True)  # Field name made lowercase.
    original_po_field = models.CharField(db_column='Original_PO#', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    arma_po_field = models.CharField(db_column='ARMA_PO#', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    replacement_unit_s_n = models.CharField(db_column='Replacement_Unit_S/N', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    return_s20 = models.CharField(db_column='Return_S20', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nus_data'


class PermissionControl(models.Model):
    user_id = models.IntegerField()
    page_name = models.CharField(max_length=255)
    permission = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'permission_control'
        unique_together = (('user_id', 'page_name', 'permission'),)


class RmaSoPo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rma = models.CharField(db_column='RMA', unique=True, max_length=12, blank=True, null=True)  # Field name made lowercase.
    so = models.CharField(db_column='SO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rma_so_po'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=500, blank=True, null=True)
    user_password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
