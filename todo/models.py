from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "todo";     

# class Member(models.Model):
#     name = models.CharField(max_length=45)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=45)
#     last_modified_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table = "member";    

class Friendship(models.Model):
    name = models.CharField(max_length=45)
    friendid = models.CharField(max_length=45)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "friendship" ;  

class Msg(models.Model):
    name = models.CharField(max_length=45)
    message = models.CharField(max_length=3000)
    targetid = models.CharField(max_length=45)
    messageimage = models.CharField(max_length=45,null=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "message" ;  



class Members(models.Model):
    mem_name = models.CharField(max_length=45)
    emailid = models.CharField(max_length=200)
    password = models.CharField(max_length=45)
    gender = models.CharField(max_length=45, blank=True, null=True)
    company = models.CharField(max_length=60, blank=True, null=True)
    companyen = models.CharField(max_length=60, blank=True, null=True)
    position = models.CharField(max_length=60, blank=True, null=True)
    positionen = models.CharField(max_length=60, blank=True, null=True)
    skill = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    bday = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'members'


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_modified_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    membername = models.CharField(max_length=30)
    memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    email = models.CharField(max_length=100)
    class Meta:
        db_table = 'articles'

class Movies(models.Model):
    title = models.CharField(max_length=45)
    url = models.CharField(max_length=300)

    class Meta:
        db_table = 'movies'



class Economist(models.Model):
    title = models.CharField(max_length=45)
    url = models.CharField(max_length=200)

    class Meta:
        db_table = 'economist'

class Adcount(models.Model):
    adname = models.CharField(max_length=45)
    count = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'Adcount'
# class Members(models.Model):
#     mem_name = models.CharField(max_length=45)
#     emailid = models.CharField(max_length=200)
#     password = models.CharField(max_length=45)
#     gender = models.CharField(max_length=45, blank=True, null=True)
#     company = models.CharField(max_length=60, blank=True, null=True)
#     companyen = models.CharField(max_length=60, blank=True, null=True)
#     position = models.CharField(max_length=60, blank=True, null=True)
#     positionen = models.CharField(max_length=60, blank=True, null=True)
#     skill = models.CharField(max_length=45, blank=True, null=True)
#     language = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'members'
#         db_table = 'economist'
