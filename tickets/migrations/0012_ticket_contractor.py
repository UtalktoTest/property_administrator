# Generated by Django 4.0.4 on 2022-05-23 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_ticketappoinment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='contractor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.suppliers'),
        ),
    ]
