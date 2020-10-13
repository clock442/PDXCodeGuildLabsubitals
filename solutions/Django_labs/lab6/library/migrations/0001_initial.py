# Generated by Django 3.1.1 on 2020-10-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
            ],
        ),
    ]
