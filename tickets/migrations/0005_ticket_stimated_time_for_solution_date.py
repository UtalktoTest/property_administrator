# Generated by Django 4.0.4 on 2022-05-31 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_maintanenceissuetype_work_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='stimated_time_for_solution_date',
            field=models.DateField(default=None, null=True),
        ),
    ]