# Generated by Django 3.2.12 on 2022-05-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0016_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
    ]
