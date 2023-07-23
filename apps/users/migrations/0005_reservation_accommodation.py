# Generated by Django 4.2.3 on 2023-07-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_reservation_choise_alter_reservation_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='accommodation',
            field=models.CharField(choices=[('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната'), ('Общая комната', 'Общая комната')], default=1, max_length=250),
            preserve_default=False,
        ),
    ]
