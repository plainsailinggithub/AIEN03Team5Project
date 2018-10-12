# Generated by Django 2.1.1 on 2018-10-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('membername', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_name', models.CharField(max_length=45)),
                ('emailid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=45)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('company', models.CharField(blank=True, max_length=60, null=True)),
                ('companyen', models.CharField(blank=True, max_length=60, null=True)),
                ('position', models.CharField(blank=True, max_length=60, null=True)),
                ('positionen', models.CharField(blank=True, max_length=60, null=True)),
                ('skill', models.CharField(blank=True, max_length=45, null=True)),
                ('language', models.CharField(blank=True, max_length=45, null=True)),
                ('img', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'members',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='memberid',
            field=models.ForeignKey(blank=True, db_column='memberid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Members'),
        ),
    ]
