# Generated by Django 4.0.4 on 2022-05-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_access',
            field=models.BooleanField(default=False),
        ),
    ]
