# Generated by Django 4.0.4 on 2022-05-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0004_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='47181578-244d-4560-94a4-7f9aac92e6fd', max_length=120, primary_key=True, serialize=False),
        ),
    ]