from django.db import models

class Admin(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    grantadmin = models.ForeignKey('self', models.DO_NOTHING, db_column='GrantAdmin')  # Field name made lowercase.
    granttime = models.DateTimeField(db_column='GrantTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


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


class Buycourse(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey('Course', models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    buytime = models.DateTimeField(db_column='BuyTime')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=100)  # Field name made lowercase.
    iscomplete = models.IntegerField(db_column='IsComplete')  # Field name made lowercase.
    completetime = models.DateTimeField(db_column='CompleteTime')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buycourse'
        unique_together = (('userid', 'cid'),)


class Completematerial(models.Model):
    cmid = models.ForeignKey('Coursematerial', models.DO_NOTHING, db_column='CMID',
                             primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    completetime = models.DateTimeField(db_column='CompleteTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'completematerial'
        unique_together = (('cmid', 'userid'),)


class Contain(models.Model):
    userid = models.ForeignKey('Playlist', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    name = models.ForeignKey('Playlist', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    cmid = models.ForeignKey('Coursematerial', models.DO_NOTHING, db_column='CMID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contain'
        unique_together = (('userid', 'name', 'cmid'),)


class Course(models.Model):
    cid = models.AutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    icon = models.TextField(db_column='Icon')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost')  # Field name made lowercase.
    primarytopic = models.ForeignKey('Topic', models.DO_NOTHING, db_column='PrimaryTopic')  # Field name made lowercase.
    enrollnumber = models.IntegerField(db_column='EnrollNumber', blank=True, null=True)  # Field name made lowercase.
    avgrate = models.IntegerField(db_column='AvgRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Coursematerial(models.Model):
    cmid = models.AutoField(db_column='CMID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursematerial'
        unique_together = (('cmid', 'cid'),)


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


class Faculty(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=200)  # Field name made lowercase.
    affiliation = models.CharField(db_column='Affiliation', max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=300)  # Field name made lowercase.
    grantadmin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='GrantAdmin')  # Field name made lowercase.
    granttime = models.DateTimeField(db_column='GrantTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty'


class Interested(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID',
                               primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interested'
        unique_together = (('userid', 'cid'),)


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


class Secondarytopic(models.Model):
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CID', primary_key=True)  # Field name made lowercase.
    tid = models.ForeignKey('Topic', models.DO_NOTHING, db_column='TID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'secondarytopic'
        unique_together = (('cid', 'tid'),)


class Topic(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic'


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
