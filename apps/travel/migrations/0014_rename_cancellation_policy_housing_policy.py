# Generated by Django 4.2.3 on 2023-08-04 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_alter_housereservation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housing',
            old_name='cancellation_policy',
            new_name='policy',
        ),
    ]
