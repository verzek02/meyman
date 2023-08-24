# Generated by Django 4.2.3 on 2023-08-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_alter_housingreservation_check_in_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amenities',
            new_name='outside',
        ),
        migrations.AlterField(
            model_name='housing',
            name='region',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='destination',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда'),
        ),
    ]
