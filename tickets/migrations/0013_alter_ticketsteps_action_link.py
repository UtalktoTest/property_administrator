# Generated by Django 4.0.4 on 2022-05-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_ticket_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsteps',
            name='action_link',
            field=models.URLField(default=None, max_length=120, null=True),
        ),
    ]