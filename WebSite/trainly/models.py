# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=300)  # Field name made lowercase.
    profilepict = models.CharField(db_column='ProfilePict', max_length=50)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=200)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
