# Generated by Django 3.2.12 on 2022-06-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0018_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=10, max_length=120),
        ),
    ]