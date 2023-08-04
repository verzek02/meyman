# Generated by Django 4.2.3 on 2023-08-04 06:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 4))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 4))], verbose_name='Выезд')),
                ('adults', models.PositiveIntegerField(default=1, verbose_name='Взрослые(от 18 лет)')),
                ('teens', models.PositiveIntegerField(default=0, verbose_name='Подростки(от 13-18 лет)')),
                ('children', models.PositiveIntegerField(default=0, verbose_name='Дети(от 2-12 лет)')),
                ('infants', models.PositiveIntegerField(default=0, verbose_name='Младенцы(младше 2)')),
                ('pets', models.PositiveIntegerField(default=0, verbose_name='Домашние животные')),
            ],
            options={
                'verbose_name': 'Бронь жилья',
                'verbose_name_plural': 'Бронь жилья',
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housing_name', models.CharField(max_length=255, verbose_name='Название места жительства')),
                ('image', models.ImageField(upload_to='images/housing/', verbose_name='Изображение места жительства')),
                ('description', models.TextField(verbose_name='Описание места жительства')),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена за ночь')),
                ('bathrooms', models.PositiveIntegerField(default=1, verbose_name='Количество ванн')),
                ('beds', models.PositiveIntegerField(default=1, verbose_name='Количество кроватей')),
                ('location', models.CharField(max_length=255, verbose_name='местоположение жилища')),
                ('check_in_time_start', models.TimeField(verbose_name='Заезд С')),
                ('check_in_time_end', models.TimeField(verbose_name='Заезд До')),
                ('check_out_time_start', models.TimeField(verbose_name='Отъезд С')),
                ('check_out_time_end', models.TimeField(verbose_name='Отъезд До')),
                ('region', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=255, verbose_name='Область')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('stars', models.PositiveIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), (0, 'Без звезд')], default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Количество звезд')),
                ('housing_type', models.CharField(choices=[('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Апартаменты', 'Апартаменты'), ('Гостевые дома', 'Гостевые дома'), ('Санатории', 'Санатории')], max_length=255, verbose_name='Тип жилья')),
                ('accommodation_type', models.CharField(choices=[('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната'), ('Общая комната', 'Общая комната')], max_length=255, verbose_name='Тип размещения')),
                ('bedrooms', models.CharField(choices=[('1 спальня', '1 спальня'), ('2 спальни', '2 спальни'), ('Больше 3 спален', 'Больше 3 спален')], default='Не включено', max_length=255, verbose_name='Количество спален')),
                ('bed_type', models.CharField(choices=[('Отдельные', 'Отдельные'), ('Двуспальная', 'Двуспальная'), ('Больше 3х', 'Больше 3х'), ('Kingsize', 'Kingsize'), ('Queensize ', 'Queensize ')], max_length=255, verbose_name='Тип кроватей')),
                ('food_type', models.CharField(choices=[('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('Не включено', 'Не включено'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=255, verbose_name='Тип питания')),
                ('parking_service', models.CharField(choices=[('free', 'Да, бесплатно'), ('paid', 'Да, платно'), ('no', 'Нет')], default='no', max_length=10, verbose_name='Услуги парковки')),
                ('parking_cost_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Стоимость парковки в US$ (за день)')),
                ('parking_location', models.CharField(blank=True, choices=[('На территории', 'На территории'), ('За территорией', 'За территорией')], max_length=50, null=True, verbose_name='Где находится парковка?')),
                ('housing_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('free_internet', 'Бесплатный интернет'), ('spa_services', 'Спа услуги'), ('restaurant', 'Ресторан'), ('Спортивный зал', 'Спортивный зал'), ('pool', 'Бассейн'), ('airport_transfer', 'Трансфер от/до аэропорта'), ('fitness', 'Фитнес'), ('pet_allowed', 'Можно с питомцами'), ('indoor_pool', 'Крытый бассейн'), ('non_smoking_rooms', 'Номера для некурящих'), ('wifi', 'Wifi'), ('room_service', 'Доставка еды и напитков в номер'), ('coffee_teapot', 'Кофеварка/чайник'), ('bar', 'Бар'), ('garden_furniture', 'Садовая мебель'), ('sun_terrace', 'Терасса для загара'), ('garden', 'Сад'), ('wine_champagne', 'Вино/шампанское (платно)'), ('kids_menu', 'Детское меню (платно)'), ('breakfast_in_room', 'Завтрак в номер'), ('breakfast_paid', 'Завтрак включен в стоимость проживания?'), ('free_wifi', 'Бесплатный Wi-Fi на территории всего отеля'), ('daily_cleaning', 'Ежедневная уборка'), ('laundry_service', 'Услуги по глажению одежды (платно)'), ('paid_cleaning', 'Химчистка (платно)'), ('paid_laundry', 'Прачечная (платно)'), ('fax_xerox', 'Факс/ксерокопирование (платно)'), ('conference_banquet_hall', 'Конференц-зал/банкетный зал (платно)'), ('fire_extinguishers', 'Огнетушители'), ('smoke_detectors', 'Датчики дыма'), ('outdoor_surveillance', 'Видеонаблюдения снаружи здания'), ('public_areas_surveillance', 'Видеонаблюдения в местах общего пользования'), ('security_alarm', 'Охранная сигнализация'), ('full_time_security', 'Круглосуточная охрана'), ('safe', 'Сейф'), ('invoices_issued', 'Выдаются счета'), ('lockers', 'Запирающиеся шкафчики'), ('concierge_service', 'Услуги консьержа'), ('atm_on_site', 'Банкомат на территории отеля'), ('luggage_storage', 'Хранение багажа'), ('express_check_in', 'Ускоренная регистрация'), ('full_time_front_desk', 'Круглосуточная стойка регистрации'), ('transfer_paid', 'Трансфер (платно)'), ('food_delivery_to_room_paid', 'Доставка продуктов питания в номер (платно)'), ('smoking_areas', 'Места для курения'), ('air_conditioner', 'Кондиционер'), ('heating', 'Отопление'), ('car_rental', 'Прокат автомобилей'), ('packed_lunches', 'Упакованные ланчи'), ('ironing_facilities', 'Гладильные принадлежности'), ('buffet_breakfast', 'Завтрак "шведский стол"'), ('free_instant_coffee', 'Бесплатный растворимый кофе'), ('free_tea', 'Бесплатный чай'), ('happy_hour', 'Счастливый час'), ('special_diet_menu', 'Специальное диетическое меню'), ('taxi_service', 'Служба такси'), ('internet_business_center', 'Бизнес-центр с доступом в Интернет'), ('facial_treatments', 'Процедуры для лица'), ('foot_massage', 'Массаж ног'), ('full_body_massage', 'Массаж всего тела'), ('hammam', 'Хаммам'), ('manual_massage', 'Ручной массаж'), ('head_massage', 'Массаж головы'), ('massage', 'Массаж'), ('neck_massage', 'Массаж шеи'), ('steam_room', 'Паровая комната'), ('currency_exchange', 'Обмен валюты'), ('bell_staff_porter', 'Швейцар'), ('individual_check_in_check_out', 'Индивидуальная регистрация заезда/отъезда'), ('dry_cleaning', 'Сухая чистка'), ('shoe_shine', 'Чистка обуви'), ('kids_playground', 'Детская площадка'), ('allow_children', 'C детьми?'), ('allow_pets', 'C домашними животными'), ('pets_paid', 'Берете ли вы плату за домашних животных?'), ('Парковка', 'Парковка')], max_length=255, verbose_name='Удобства в объекте')),
                ('room_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('air_conditioner', 'Кондиционер'), ('hair_dryer', 'Фен'), ('washing_machine', 'Стиральная машина'), ('iron', 'Утюг'), ('dryer', 'Сушильная машина'), ('fridge', 'Холодильник'), ('tv', 'Телевизор'), ('microwave', 'Микроволновка'), ('heating', 'Отопление'), ('sofa_bed', 'Диван-кровать'), ('folding_bed', 'Раскладная кровать'), ('Двуспальная кровать', 'Двуспальная кровать'), ('wardrobe', 'Шкаф или гардероб'), ('linen', 'Белье'), ('clothes_hanger', 'Вешалка для одежды'), ('complimentary_toiletries', 'Бесплатные туалетно-косметические принадлежности'), ('toilet_paper', 'Туалетная бумага'), ('kitchen_utensils', 'Кухонные принадлежности'), ('electric_kettle', 'Электрический чайник'), ('city_view', 'Вид на город'), ('garden_view', 'Вид на сад'), ('high_toilet', 'Высокий туалет'), ('toilet_with_handles', 'Туалет с поручнями'), ('accessible_to_disabled_guests', 'Подходит для гостей с ограниченными возможностями'), ('work_desk', 'Рабочий стол'), ('room_cleaning', 'Уборка'), ('coffee_teapot', 'Кофеварка/чайник'), ('cable_satellite_tv', 'Кабельное / спутниковое телевидение'), ('bidet', 'Биде'), ('connecting_rooms_available', 'Доступны смежные номера'), ('room_service', 'Обслуживание номеров'), ('safe', 'Безопасный'), ('sitting_area', 'Зона отдыха'), ('telephone', 'Телефон'), ('bottled_water', 'Бутилированная вода'), ('Сейф', 'Сейф'), ('laptop_safe_box', 'Сейф для ноутбука'), ('private_bathroom', 'Частные ванные комнаты'), ('wake_up_service', 'Услуга будильник / будильник'), ('minibar', 'Минибар'), ('flat_screen_tv', 'Телевизор с плоским экраном'), ('bath_or_shower', 'Ванна/душ'), ('Комоды', 'Комоды'), ('Мини кухня', 'Мини кухня'), ('Камин', 'Камин'), ('Закуски', 'Закуски'), ('2 комнаты', '2 комнаты')], max_length=255, verbose_name='Удобства в номере')),
                ('without_credit_card', models.CharField(choices=[('Нет', 'Нет'), ('Да', 'Да')], default=True, max_length=25, verbose_name='Без банковской карты')),
                ('free_cancellation', models.CharField(choices=[('Нет', 'Нет'), ('Да', 'Да')], default=False, max_length=25, verbose_name='Бесплатная отмена')),
                ('payment_type', models.CharField(choices=[('К оплате сейчас', 'К оплате сейчас'), ('Предоплата', 'Предоплата'), ('Оплата наличными', 'Оплата наличными')], default='К оплате сейчас', max_length=50, verbose_name='Оплата')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='человеко-понятный url')),
            ],
            options={
                'verbose_name': 'Жильё',
                'verbose_name_plural': 'Жильё',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Апартаменты',
                'verbose_name_plural': 'Апартаменты',
            },
            bases=('travel.housing',),
        ),
        migrations.CreateModel(
            name='GuestHouse',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Гостиница',
                'verbose_name_plural': 'Гостиницы',
            },
            bases=('travel.housing',),
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Хостел',
                'verbose_name_plural': 'Хостелы',
            },
            bases=('travel.housing',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
            bases=('travel.housing',),
        ),
        migrations.CreateModel(
            name='Sanatorium',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Санаторий',
                'verbose_name_plural': 'Санатории',
            },
            bases=('travel.housing',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('Замечательно', 'Замечательно'), ('Отлично', 'Отлично'), ('Хорошо', 'Хорошо'), ('Неплохо', 'Неплохо'), ('Не оценено', 'Не оценено')], default='0', max_length=20)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_received', to='travel.housing')),
            ],
        ),
    ]
