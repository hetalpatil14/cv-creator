# Generated by Django 5.1 on 2024-09-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_person_image_alter_person_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
