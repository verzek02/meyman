# Generated by Django 4.2.3 on 2023-08-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_remove_housing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='images',
            field=models.CharField(default=1, max_length=1000, verbose_name='Пути к изображениям места жительства'),
            preserve_default=False,
        ),
    ]
