# Generated by Django 5.1 on 2024-09-09 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_activity_person_address_person_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='honors',
            new_name='honor',
        ),
    ]
