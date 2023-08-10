# Generated by Django 4.2.3 on 2023-08-10 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_housereservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='housing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travel.housing', verbose_name='Название места жительства'),
        ),
        migrations.AlterField(
            model_name='room',
            name='housing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.housing', verbose_name='Название места жительства'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(upload_to='images/rooms', verbose_name='Изображение'),
        ),
    ]
