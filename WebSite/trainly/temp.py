# generate by django
# When use, move to model.py

from django.db import models


class Adminposition(models.Model):
    userid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminposition'
        unique_together = (('userid', 'position'),)


class Answer(models.Model):
    userid = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    qid = models.ForeignKey('Question', models.DO_NOTHING, db_column='QID')  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'answer'
        unique_together = (('userid', 'qid'),)


class Contain(models.Model):
    userid = models.ForeignKey('Playlist', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    name = models.ForeignKey('Playlist', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    cmid = models.ForeignKey('Coursematerial', models.DO_NOTHING, db_column='CMID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contain'
        unique_together = (('userid', 'name', 'cmid'),)


class Createcourse(models.Model):
    userid = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'createcourse'
        unique_together = (('userid', 'cid'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Downloadable(models.Model):
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=500)  # Field name made lowercase.
    size = models.TextField(db_column='Size')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'downloadable'


class Likequestion(models.Model):
    qid = models.ForeignKey('Question', models.DO_NOTHING, db_column='QID')  # Field name made lowercase.
    userid = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'likequestion'
        unique_together = (('userid', 'qid'),)


class Link(models.Model):
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200)  # Field name made lowercase.
    tagvedio = models.IntegerField(db_column='TagVedio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'link'


class Phone(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone'
        unique_together = (('userid', 'phone'),)


class Playlist(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist'
        unique_together = (('userid', 'name'),)


class Post(models.Model):
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'


class Question(models.Model):
    qid = models.AutoField(db_column='QID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    askby = models.ForeignKey('User', models.DO_NOTHING, db_column='AskBy')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'


class Quiz(models.Model):
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    passingscore = models.IntegerField(db_column='PassingScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quiz'


class Quizquestion(models.Model):
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.
    indicator = models.IntegerField(db_column='Indicator')  # Field name made lowercase.
    feedback = models.TextField(db_column='Feedback')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quizquestion'
        unique_together = (('cmid', 'number'),)


class Related(models.Model):
    qid = models.ForeignKey(Question, models.DO_NOTHING, db_column='QID',
                            primary_key=True)  # Field name made lowercase.
    cmid = models.ForeignKey(Coursematerial, models.DO_NOTHING, db_column='CMID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'related'
        unique_together = (('qid', 'cmid'),)
