# Generated by Django 4.0.4 on 2022-05-16 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='property_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='units',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.unittypes'),
        ),
        migrations.AddField(
            model_name='tenants',
            name='landlord',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tenants',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.units'),
        ),
        migrations.AddField(
            model_name='propertycities',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.propertycountries'),
        ),
        migrations.AddField(
            model_name='properties',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.propertycities'),
        ),
        migrations.AddField(
            model_name='properties',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='properties',
            name='property_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.propertytypes'),
        ),
        migrations.AddField(
            model_name='links',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
