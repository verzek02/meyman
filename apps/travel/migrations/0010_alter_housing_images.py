# Generated by Django 4.2.3 on 2023-08-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_alter_housing_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='images',
            field=models.ImageField(upload_to='images/housing/', verbose_name='Изображения места жительства'),
        ),
    ]
