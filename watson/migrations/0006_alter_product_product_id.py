# Generated by Django 3.2.12 on 2022-05-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0005_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='9db03012-848f-4f3d-93a9-4475a5d6bdd4', max_length=120, primary_key=True, serialize=False),
        ),
    ]
