# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

    class Meta:
        managed = True
        db_table = 'members'
