# Generated by Django 4.0.4 on 2022-05-20 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_customuser_plan_expired_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan_expired_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 16, 5, 27, 940530)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 16, 5, 27, 940530)),
        ),
    ]
