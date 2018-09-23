from django.db import models

# Create your models here.


class Articles(models.Model):
    # id
    # member id --> To get member name、 member email
    title = models.CharField(max_length = 100)
    content = models.TextField()
    last_modified_time = models.DateTimeField(auto_now = True)
    create_time = models.DateTimeField(auto_now_add = True)
    membername = models.CharField(max_length = 30)

    class Meta:
        db_table = 'articles'