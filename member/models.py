from django.db import models

# Create your models here.


class Members(models.Model):
    mem_name = models.CharField(max_length=45)
    emailid = models.CharField(max_length=200)
    password = models.CharField(max_length=45)

    class Meta:
        db_table = 'members'
