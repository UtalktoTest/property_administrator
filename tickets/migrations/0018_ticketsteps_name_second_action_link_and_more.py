# Generated by Django 4.0.4 on 2022-05-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_remove_ticket_target_completion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsteps',
            name='name_second_action_link',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ticketsteps',
            name='second_action_link',
            field=models.URLField(default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='ticketpayment',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
