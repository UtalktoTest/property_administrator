# Generated by Django 4.0.4 on 2022-05-11 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_propertytypes_unittypes_alter_units_unit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='_property_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='properties.propertytypes'),
        ),
    ]
