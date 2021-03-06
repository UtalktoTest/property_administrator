# Generated by Django 3.2.12 on 2022-05-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_date', models.JSONField()),
                ('adults_information', models.JSONField()),
                ('current_address', models.CharField(max_length=400)),
                ('current_landlord_name', models.CharField(max_length=100)),
                ('current_landlord_phone', models.CharField(max_length=100)),
                ('duration_of_lease', models.CharField(max_length=25)),
                ('expected_renting_duration', models.CharField(max_length=100)),
                ('family_income', models.CharField(max_length=50)),
                ('facebook_account', models.CharField(default='', max_length=500)),
                ('length_of_time_at_current_address', models.CharField(max_length=400)),
                ('link_to_schedule_view_sent', models.BooleanField(default=False)),
                ('max_score', models.IntegerField(default=80)),
                ('manual_questions_reviewed', models.BooleanField(default=False)),
                ('number_of_adults', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('pets', models.CharField(max_length=100)),
                ('previous_unit_time', models.CharField(max_length=255)),
                ('preferred_move_in_date', models.DateField()),
                ('reason_for_moving', models.TextField()),
                ('reason_for_rejection', models.CharField(default='', max_length=250)),
                ('rejected', models.BooleanField(default=False)),
                ('relevant_information', models.TextField()),
                ('work_references_checked', models.BooleanField(default=False)),
                ('work_references_passed', models.BooleanField(default=False)),
                ('living_references_checked', models.BooleanField(default=False)),
                ('living_references_passed', models.BooleanField(default=False)),
                ('score', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('viewing_date', models.DateTimeField(default=None, null=True)),
                ('viewing_id', models.CharField(default=None, max_length=200, null=True)),
                ('viewing_score', models.IntegerField(null=True)),
                ('viewing_comments', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('string', models.CharField(max_length=100)),
            ],
        ),
    ]
