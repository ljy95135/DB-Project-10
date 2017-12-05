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
    userID = models.AutoField(db_column='UserID', primary_key=True)
    email = models.CharField(db_column='Email', unique=True, max_length=100)
    firstName = models.CharField(db_column='FirstName', max_length=50)
    lastName = models.CharField(db_column='LastName', max_length=50)
    pw = models.CharField(db_column='PW', max_length=300)
    profilePict = models.CharField(db_column='ProfilePict', max_length=50)
    country = models.CharField(db_column='Country', max_length=50)
    city = models.CharField(db_column='City', max_length=50)
    street = models.CharField(db_column='Street', max_length=200)
    postalCode = models.CharField(db_column='PostalCode', max_length=20)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return str(self.userID) + ":" + self.email


class Admin(models.Model):
    userID = models.ForeignKey('User', db_column='UserID', primary_key=True)
    grantAdmin = models.ForeignKey('self', models.DO_NOTHING, db_column='GrantAdmin')  # Field name made lowercase.
    grantTime = models.DateTimeField(db_column='GrantTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'

    def __str__(self):
        return self.userID.__str__()


class Faculty(models.Model):
    userID = models.ForeignKey('User', db_column='UserID', primary_key=True)
    website = models.CharField(db_column='Website', max_length=200)
    affiliation = models.CharField(db_column='Affiliation', max_length=50)
    title = models.CharField(db_column='Title', max_length=300)
    grantAdmin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='GrantAdmin')
    grantTime = models.DateTimeField(db_column='GrantTime')

    class Meta:
        managed = False
        db_table = 'faculty'

    def __str__(self):
        return self.userID.__str__()
