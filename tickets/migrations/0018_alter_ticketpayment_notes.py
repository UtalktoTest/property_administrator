# Generated by Django 4.0.4 on 2022-05-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_remove_ticket_target_completion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketpayment',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
