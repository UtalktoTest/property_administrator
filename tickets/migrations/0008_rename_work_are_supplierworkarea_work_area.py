# Generated by Django 4.0.4 on 2022-05-20 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_rename_work_are_suppliers_work_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierworkarea',
            old_name='work_are',
            new_name='work_area',
        ),
    ]