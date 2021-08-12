# Generated by Django 3.2.6 on 2021-08-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210811_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
