# Generated by Django 4.2.3 on 2023-08-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_rename_amenities_room_outside_alter_housing_region_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='outside',
            new_name='amenities',
        ),
    ]