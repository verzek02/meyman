# Generated by Django 4.2.3 on 2023-08-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='transfer_image',
            field=models.ImageField(default=1, upload_to='transfer/housing', verbose_name='Изображение автомобиля'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TransferImage',
        ),
    ]
