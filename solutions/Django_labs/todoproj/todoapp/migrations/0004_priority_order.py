# Generated by Django 3.1.1 on 2020-09-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todoitem_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]