from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "todo";   

class Member(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=45)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "member";    

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