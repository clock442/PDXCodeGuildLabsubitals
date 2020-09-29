# Generated by Django 3.1.1 on 2020-09-29 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='todoitems', to='todoapp.priority'),
            preserve_default=False,
        ),
    ]
