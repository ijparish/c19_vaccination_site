# Generated by Django 3.2 on 2021-04-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_auto_20210421_1932'),
        ('app', '0002_auto_20210421_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appoint',
            field=models.ManyToManyField(to='clinics.ScheduleTime'),
        ),
    ]
