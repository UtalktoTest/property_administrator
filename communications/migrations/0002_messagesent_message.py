# Generated by Django 4.0.4 on 2022-05-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesent',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
