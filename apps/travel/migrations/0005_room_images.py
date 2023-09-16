# Generated by Django 4.2.3 on 2023-09-16 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_remove_room_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='travel.roomimage'),
        ),
    ]
