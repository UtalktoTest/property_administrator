# Generated by Django 4.0.4 on 2022-05-18 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0002_messagesent_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagesent',
            old_name='message_subject',
            new_name='subject',
        ),
    ]