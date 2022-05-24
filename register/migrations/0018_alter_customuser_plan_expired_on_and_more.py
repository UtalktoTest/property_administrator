# Generated by Django 4.0.4 on 2022-05-23 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_alter_customuser_plan_expired_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan_expired_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 11, 39, 38, 175697)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 23, 15, 39, 38, 175697, tzinfo=utc)),
        ),
    ]
