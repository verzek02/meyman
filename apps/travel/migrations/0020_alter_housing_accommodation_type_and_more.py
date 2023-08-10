# Generated by Django 4.2.3 on 2023-08-10 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0019_alter_housing_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='accommodation_type',
            field=models.CharField(choices=[('Общая комната', 'Общая комната'), ('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната')], max_length=50, verbose_name='Тип размещения'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='food_type',
            field=models.CharField(choices=[('Не включено', 'Не включено'), ('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=50, verbose_name='Тип питания'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='housing_type',
            field=models.CharField(choices=[('Квартиры', 'Квартиры'), ('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Дома', 'Дома'), ('Санатории', 'Санатории')], max_length=50, verbose_name='Тип жилья'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='parking',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Да, бесплатно', 'Да, бесплатно'), ('Да, платно', 'Да, платно')], default='Нет', max_length=50, verbose_name='Услуги парковки'),
        ),
        migrations.AlterField(
            model_name='room',
            name='policy',
            field=models.CharField(choices=[('До 00:00 в день заезда', 'До 00:00 в день заезда'), ('В любое время', 'В любое время')], default=None, max_length=50, verbose_name='Правила бесплатной отмены'),
        ),
    ]
