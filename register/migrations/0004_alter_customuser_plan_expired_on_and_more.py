# Generated by Django 4.0.4 on 2022-05-20 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_merge_20220520_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan_expired_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 12, 10, 23, 861131)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 12, 10, 23, 861131)),
        ),
    ]
