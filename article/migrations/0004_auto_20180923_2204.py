# Generated by Django 2.1.1 on 2018-09-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180923_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='last_modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
