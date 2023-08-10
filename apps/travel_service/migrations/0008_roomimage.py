# Generated by Django 4.2.3 on 2023-08-10 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0007_alter_transfer_transfer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_image', models.ImageField(upload_to='rooms', verbose_name='Изображения Трансфера')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_images', to='travel_service.transfer')),
            ],
            options={
                'verbose_name': 'Изображение номера',
                'verbose_name_plural': 'Изображения номеров',
            },
        ),
    ]
