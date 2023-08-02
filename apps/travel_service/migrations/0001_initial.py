# Generated by Django 4.2.3 on 2023-08-02 15:55

import datetime
import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область нахождения машины')),
                ('image', models.ImageField(upload_to='images/car/', verbose_name='Изображение автомобиля')),
                ('category', models.CharField(choices=[('Легковушка', 'Легковушка'), ('Минивэн', 'Минивэн'), ('Внедорожник', 'Внедорожник'), ('Автобус', 'Автобус'), ('Кроссовер', 'Кроссовер')], max_length=255, verbose_name='Категория автомобиля')),
                ('transmission', models.CharField(choices=[('Механическая', 'Механическая'), ('Автоматическая', 'Автоматическая'), ('Другое', 'Другое')], max_length=255, verbose_name='Тип коробки передач')),
                ('steering', models.CharField(choices=[('Левый', 'Левый'), ('Правый', 'Правый')], max_length=50, verbose_name='Руль')),
                ('body_type', models.CharField(choices=[('Седан', 'Седан'), ('Купе', 'Купе'), ('Хэтчбек', 'Хэтчбек'), ('Лифтбек', 'Лифтбек'), ('Фастбэк', 'Фастбэк'), ('Универсал', 'Универсал'), ('Кроссовер', 'Кроссовер'), ('Внедорожник', 'Внедорожник'), ('Легковой фургон', 'Легковой фургон'), ('Минивэн', 'Минивэн'), ('Компактвэн', 'Компактвэн'), ('Микровэн', 'Микровэн'), ('Кабриолет', 'Кабриолет'), ('Родстер', 'Родстер'), ('Тарга', 'Тарга'), ('Ландо', 'Ландо'), ('Лимузин', 'Лимузин')], max_length=255, verbose_name='Тип кузова')),
                ('drive_type', models.CharField(choices=[('Передний', 'Передний'), ('Задний', 'Задний'), ('Полный', 'Полный')], max_length=255, verbose_name='Тип привода')),
                ('fuel_type', models.CharField(choices=[('Бензин', 'Бензин'), ('Бензин/Газ', 'Бензин/Газ'), ('Газ', 'Газ'), ('Дизель', 'Дизель'), ('Электрический', 'Электрический'), ('Другое', 'Другое')], max_length=255, verbose_name='Тип топлива')),
                ('passenger_capacity', models.CharField(choices=[('2', '2 пассажира'), ('5', '5 пассажиров'), ('8', '8 пассажиров'), ('Другое', 'Другое')], max_length=255, verbose_name='Вместимость пассажиров')),
                ('condition', models.CharField(choices=[('Хорошее', 'Хорошее'), ('Идеальное', 'Идеальное'), ('Новое', 'Новое')], max_length=255, verbose_name='Состояние автомобиля')),
                ('currency', models.CharField(choices=[('Рубль', 'Рубль'), ('Сом', 'Сом'), ('USD', 'USD')], max_length=10, verbose_name='Валюта')),
                ('minimum_age', models.CharField(choices=[('18', '18 лет'), ('20', '20 лет'), ('22', '22 года'), ('24', '24 года'), ('26', '26 лет'), ('28', '28 лет'), ('30', '30 лет'), ('32', '32 года'), ('34', '34 года'), ('36', '36 лет'), ('38', '38 лет'), ('40', '40 лет'), ('42', '42 года'), ('44', '44 года'), ('46', '46 лет'), ('48', '48 лет'), ('50', '50 лет')], max_length=2, verbose_name='Минимальный возраст')),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма аренды (Сутки)')),
                ('car_address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('brand', models.CharField(choices=[('Мерседес-бенц', 'Мерседес-бенц'), ('Лендровер', 'Лендровер'), ('БМВ', 'БМВ'), ('Вольво', 'Вольво'), ('Шевролед', 'Шевролед'), ('Фольксваген', 'Фольксваген'), ('Хонда', 'Хонда'), ('Ауди', 'Ауди'), ('Хендай', 'Хендай'), ('Форд', 'Форд'), ('Киа', 'Киа'), ('Лексус', 'Лексус'), ('Мицубиси', 'Мицубиси'), ('Рено', 'Рено'), ('Опель', 'Опель'), ('Субару', 'Субару'), ('Мазда', 'Мазда'), ('Порше', 'Порше'), ('Дэу', 'Дэу'), ('Лада', 'Лада'), ('Сузуки', 'Сузуки'), ('Инфинити', 'Инфинити'), ('Ссанг Йонг', 'Ссанг Йонг'), ('Ниссан', 'Ниссан'), ('Тойота', 'Тойота')], max_length=50, verbose_name='Марка автомобиля')),
                ('model', models.CharField(max_length=50, verbose_name='Модель автомобиля')),
                ('color', models.CharField(blank=True, choices=[('Серебристый', 'Серебристый'), ('Черный', 'Черный'), ('Белый', 'Белый'), ('Серый', 'Серый'), ('Бежевый', 'Бежевый'), ('Бирюзовый', 'Бирюзовый'), ('Бордовый', 'Бордовый'), ('Бронза', 'Бронза'), ('Хамелеон', 'Хамелеон'), ('Жёлтый', 'Жёлтый'), ('Зеленый', 'Зеленый'), ('Золотоый', 'Золотоый'), ('Коричневый', 'Коричневый'), ('Фиолетовый', 'Фиолетовый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Сиреневый', 'Сиреневый'), ('Вишьня', 'Вишьня'), ('Баклажан', 'Баклажан'), ('Голубой', 'Голубой')], max_length=50, verbose_name='Цвет автомобиля')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска автомобиля')),
                ('description', models.TextField(blank=True, verbose_name='Описание автомобиля')),
                ('fuel_consumption', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Расход топлива на 100км')),
                ('driving_experience', models.PositiveIntegerField(verbose_name='Минимальный стаж вождения для аренды')),
                ('payment_method', models.CharField(choices=[('К оплате сейчас', 'К оплате сейчас'), ('Предоплата', 'Предоплата'), ('Оплата наличными', 'Оплата наличными')], max_length=20, verbose_name='Способ оплаты')),
                ('pickup_region', multiselectfield.db.fields.MultiSelectField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен'), ('Все', 'Все')], max_length=50, verbose_name='Регион получения')),
                ('return_region', multiselectfield.db.fields.MultiSelectField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен'), ('Все', 'Все')], max_length=50, verbose_name='Регион возврата')),
                ('has_safety_equipment', multiselectfield.db.fields.MultiSelectField(choices=[('fire_extinguisher', 'Наличие огнетушителя'), ('first_aid_kit', 'Наличие аптечки'), ('spare_wheel', 'Наличие запасного колеса'), ('airbags', 'Наличие подушка безопасности'), ('emergency_tools', 'Наличие инструментов аварийной ситуации'), ('dashboard_camera', 'Наличие авторегистратора')], max_length=100, verbose_name='Наличие системы безопасности')),
                ('air_conditioner', models.BooleanField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default=False, verbose_name='Кондиционер')),
                ('check_in_time', models.TimeField(verbose_name='Время заезда')),
                ('check_out_time', models.TimeField(verbose_name='Время отъезда')),
                ('can_arrange_pickup_return', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=10, verbose_name='Может ли клиент договориться о месте получения/возврата автомобиля')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Выезд')),
                ('adults', models.PositiveIntegerField(default=1, verbose_name='Взрослые(от 18 лет)')),
                ('teens', models.PositiveIntegerField(default=0, verbose_name='Подростки(от 13-18 лет)')),
                ('children', models.PositiveIntegerField(default=0, verbose_name='Дети(от 2-12 лет)')),
                ('infants', models.PositiveIntegerField(default=0, verbose_name='Младенцы(младше 2)')),
                ('pets', models.PositiveIntegerField(default=0, verbose_name='Домашние животные')),
            ],
            options={
                'verbose_name': 'Поиск жилья',
                'verbose_name_plural': 'Поиск жилья',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_location', models.CharField(max_length=255, verbose_name='Место получения трансфера')),
                ('destination_location', models.CharField(max_length=255, verbose_name='Куда вы хотите поехать')),
                ('pickup_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Дата получения трансфера')),
                ('pickup_time', models.TimeField(verbose_name='Время получения трансфера')),
                ('return_location', models.CharField(max_length=255, verbose_name='Место возврата трансфера')),
                ('return_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Дата возврата трансфера')),
                ('return_time', models.TimeField(verbose_name='Время возврата трансфера')),
                ('different_pickup_places', models.BooleanField(default=False, verbose_name='Разные места получения')),
                ('with_driver', models.BooleanField(default=False, verbose_name='Трансфер с водителем')),
            ],
            options={
                'verbose_name': 'Поиск трансфера',
                'verbose_name_plural': 'Поиск Трансферов',
            },
        ),
    ]
