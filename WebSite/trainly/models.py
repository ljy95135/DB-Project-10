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
    grantAdmin = models.ForeignKey('self', models.DO_NOTHING, db_column='GrantAdmin')
    grantTime = models.DateTimeField(db_column='GrantTime')

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


class Course(models.Model):
    cid = models.AutoField(db_column='CID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.TextField(db_column='Description')
    icon = models.TextField(db_column='Icon')
    date = models.DateTimeField(db_column='Date')
    cost = models.IntegerField(db_column='Cost')
    primaryTopic = models.ForeignKey('Topic', models.DO_NOTHING, db_column='PrimaryTopic')
    enrollNumber = models.IntegerField(db_column='EnrollNumber', blank=True, null=True)
    avgRate = models.IntegerField(db_column='AvgRate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'

    def __str__(self):
        return str(self.cid) + ":" + self.name


class Topic(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)

    class Meta:
        managed = False
        db_table = 'topic'

    def __str__(self):
        return self.name


class Secondarytopic(models.Model):
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID', primary_key=True)  # Field name made lowercase.
    tid = models.ForeignKey('Topic', models.DO_NOTHING, db_column='TID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'secondarytopic'
        unique_together = (('cid', 'tid'),)

    def __str__(self):
        return self.cid.__str__() + ':' + self.tid.__str__()


class BuyCourse(models.Model):
    userID = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)
    cid = models.ForeignKey('Course', models.DO_NOTHING, db_column='CID')
    buyTime = models.DateTimeField(db_column='BuyTime')
    code = models.CharField(db_column='Code', max_length=100)
    isComplete = models.IntegerField(db_column='IsComplete')
    completeTime = models.DateTimeField(db_column='CompleteTime')
    rating = models.IntegerField(db_column='Rating')
    comment = models.TextField(db_column='Comment')

    class Meta:
        managed = False
        db_table = 'buycourse'
        unique_together = (('userID', 'cid'),)

    def __str__(self):
        return self.userID.email + ':' + self.cid.name


class Interested(models.Model):
    userID = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', primary_key=True)
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID')

    class Meta:
        managed = False
        db_table = 'interested'
        unique_together = (('userID', 'cid'),)
