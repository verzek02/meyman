# Generated by Django 4.2.3 on 2023-07-22 08:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область')),
                ('housing_name', models.CharField(max_length=255, verbose_name='Название места жительства')),
                ('image', models.ImageField(upload_to='images/housing/', verbose_name='Изображение места жительства')),
                ('description', models.TextField(verbose_name='Описание места жительства')),
                ('min_and_max_price_per_night', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(500)], verbose_name='цена за ночь')),
                ('bathrooms', models.PositiveIntegerField(default=1, verbose_name='Количество ванн')),
                ('beds', models.PositiveIntegerField(default=1, verbose_name='Количество кроватей')),
                ('housing_type', models.CharField(choices=[('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Апартаменты', 'Апартаменты'), ('Гостевые дома', 'Гостевые дома'), ('Санатории', 'Санатории')], max_length=50, verbose_name='Тип жилья')),
                ('accommodation_type', models.CharField(choices=[('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната'), ('Общая комната', 'Общая комната')], max_length=255, verbose_name='Тип размещения')),
                ('bed_type', models.CharField(choices=[('Отдельные', 'Отдельные'), ('Двуспальная', 'Двуспальная'), ('Больше 3х', 'Больше 3х'), ('Kingsize', 'Kingsize'), ('Queensize ', 'Queensize ')], max_length=255, verbose_name='Тип кроватей')),
                ('food_type', models.CharField(choices=[('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('Не включено', 'Не включено'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=50, verbose_name='Тип питания')),
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
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитанно')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Когда написанно')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кому')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомление',
            },
        ),
        migrations.CreateModel(
            name='RoomAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_conditioner', models.BooleanField(default=False, verbose_name='Кондиционер')),
                ('hair_dryer', models.BooleanField(default=False, verbose_name='Фен')),
                ('washing_machine', models.BooleanField(default=False, verbose_name='Стиральная машина')),
                ('iron', models.BooleanField(default=False, verbose_name='Утюг')),
                ('dryer', models.BooleanField(default=False, verbose_name='Сушильная машина')),
                ('fridge', models.BooleanField(default=False, verbose_name='Холодильник')),
                ('tv', models.BooleanField(default=False, verbose_name='Телевизор')),
                ('microwave', models.BooleanField(default=False, verbose_name='Микроволновка')),
                ('heating', models.BooleanField(default=False, verbose_name='Отопление')),
                ('sofa_bed', models.BooleanField(default=False, verbose_name='Диван-кровать')),
                ('folding_bed', models.BooleanField(default=False, verbose_name='Раскладная кровать')),
                ('wardrobe', models.BooleanField(default=False, verbose_name='Шкаф или гардероб')),
                ('linen', models.BooleanField(default=False, verbose_name='Белье')),
                ('clothes_hanger', models.BooleanField(default=False, verbose_name='Вешалка для одежды')),
                ('complimentary_toiletries', models.BooleanField(default=False, verbose_name='Бесплатные туалетно-косметические принадлежности')),
                ('toilet_paper', models.BooleanField(default=False, verbose_name='Туалетная бумага')),
                ('kitchen', models.BooleanField(default=False, verbose_name='Кухня')),
                ('kitchen_utensils', models.BooleanField(default=False, verbose_name='Кухонные принадлежности')),
                ('electric_kettle', models.BooleanField(default=False, verbose_name='Электрический чайник')),
                ('private_entrance', models.BooleanField(default=False, verbose_name='Отдельный вход')),
                ('beach_access', models.BooleanField(default=False, verbose_name='Доступ на пляж')),
                ('outdoor_shower', models.BooleanField(default=False, verbose_name='Душ на улице')),
                ('indoor_shower', models.BooleanField(default=False, verbose_name='Душ внутри')),
                ('hot_water', models.BooleanField(default=False, verbose_name='Горячая вода')),
                ('bed_linen_towels', models.BooleanField(default=False, verbose_name='Постельное белье и полотенца')),
                ('hangers', models.BooleanField(default=False, verbose_name='Вешалки')),
                ('safety_box', models.BooleanField(default=False, verbose_name='Сейф')),
                ('clothes_storage', models.BooleanField(default=False, verbose_name='Место для хранения одежды')),
                ('entertainment', models.BooleanField(default=False, verbose_name='Развлечения')),
                ('internet_tv', models.BooleanField(default=False, verbose_name='Подключение к интернету и ТВ')),
                ('family_friendly', models.BooleanField(default=False, verbose_name='Для семей с детьми')),
                ('fireplace_grate', models.BooleanField(default=False, verbose_name='Каминная решетка')),
                ('board_games', models.BooleanField(default=False, verbose_name='Настольные игры')),
                ('heating_cooling', models.BooleanField(default=False, verbose_name='Отопление и охлаждение')),
                ('firewood', models.BooleanField(default=False, verbose_name='Дрова')),
                ('ceiling_fan', models.BooleanField(default=False, verbose_name='Потолочный вентилятор')),
                ('central_heating', models.BooleanField(default=False, verbose_name='Центральное отопление')),
                ('home_safety', models.BooleanField(default=False, verbose_name='Безопасность жилья')),
                ('video_surveillance', models.BooleanField(default=False, verbose_name='Камеры видеонаблюдения в жилье')),
                ('smoke_detector', models.BooleanField(default=False, verbose_name='Датчик дыма')),
                ('carbon_monoxide_detector', models.BooleanField(default=False, verbose_name='Датчик угарного газа')),
                ('fire_extinguisher', models.BooleanField(default=False, verbose_name='Огнетушитель')),
                ('first_aid_kit', models.BooleanField(default=False, verbose_name='Аптечка')),
                ('internet_work_area', models.BooleanField(default=False, verbose_name='Интернет и рабочее место')),
                ('kitchen_dining', models.BooleanField(default=False, verbose_name='Кухня и столовая')),
                ('guests_can_cook', models.BooleanField(default=False, verbose_name='Гости могут готовить')),
                ('dining_table', models.BooleanField(default=False, verbose_name='Обеденный стол')),
                ('location_features', models.BooleanField(default=False, verbose_name='Особенности местоположения')),
                ('separate_entrance', models.BooleanField(default=False, verbose_name='Отдельный вход')),
                ('beach_access_view', models.BooleanField(default=False, verbose_name='Доступ на пляж, вид на пляж')),
                ('outdoor_area_view', models.BooleanField(default=False, verbose_name='На улице, вид на сад')),
                ('garden_patio_balcony_private_access', models.BooleanField(default=False, verbose_name='Дворик (патио) или балкон с частным доступом')),
                ('backyard', models.BooleanField(default=False, verbose_name='Задний двор')),
                ('outdoor_furniture', models.BooleanField(default=False, verbose_name='Уличная мебель')),
                ('outdoor_dining_area', models.BooleanField(default=False, verbose_name='Обеденная зона на улице')),
                ('barbecue_area', models.BooleanField(default=False, verbose_name='Зона барбекю')),
                ('beach_equipment', models.BooleanField(default=False, verbose_name='Все необходимое для пляжа')),
                ('bicycles', models.BooleanField(default=False, verbose_name='Велосипеды')),
                ('parking_facilities', models.BooleanField(default=False, verbose_name='Парковка и объекты')),
                ('free_on_site_parking', models.BooleanField(default=False, verbose_name='Бесплатная парковка на территории')),
                ('free_street_parking', models.BooleanField(default=False, verbose_name='Бесплатная парковка на улице')),
                ('outdoor_pool', models.BooleanField(default=False, verbose_name='Бассейн: на улице')),
                ('outdoor_panoramic_pool', models.BooleanField(default=False, verbose_name='Бассейн: панорамный')),
                ('outdoor_saltwater_pool', models.BooleanField(default=False, verbose_name='Бассейн: соленая вода')),
                ('private_hydromassage_pool', models.BooleanField(default=False, verbose_name='Собственная гидромассажная ванна')),
                ('elevator', models.BooleanField(default=False, verbose_name='Лифт')),
                ('single_level_accommodation', models.BooleanField(default=False, verbose_name='Одноуровневое жилье')),
                ('services', models.BooleanField(default=False, verbose_name='Услуги')),
                ('baggage_storage', models.BooleanField(default=False, verbose_name='Можно оставить багаж')),
                ('long_term_stays', models.BooleanField(default=False, verbose_name='Разрешено длительное проживание')),
                ('self_check_in', models.BooleanField(default=False, verbose_name='Самостоятельное прибытие')),
                ('mini_safe', models.BooleanField(default=False, verbose_name='Мини-сейф')),
                ('housing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='room_amenities', to='travel.housing')),
            ],
            options={
                'verbose_name': 'Удобства в номере',
                'verbose_name_plural': 'Удобства в номере',
            },
        ),
        migrations.CreateModel(
            name='HousingAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_internet', models.BooleanField(default=False, verbose_name='Бесплатный интернет')),
                ('spa_services', models.BooleanField(default=False, verbose_name='Спа услуги')),
                ('parking', models.BooleanField(default=False, verbose_name='Парковка')),
                ('bar_or_restaurant', models.BooleanField(default=False, verbose_name='Бар/Ресторан')),
                ('pool', models.BooleanField(default=False, verbose_name='Бассейн')),
                ('airport_transfer', models.BooleanField(default=False, verbose_name='Трансфер от/до аэропорта')),
                ('fitness', models.BooleanField(default=False, verbose_name='Фитнес')),
                ('pet_allowed', models.BooleanField(default=False, verbose_name='Можно с питомцами')),
                ('indoor_pool', models.BooleanField(default=False, verbose_name='Крытый бассейн')),
                ('non_smoking_rooms', models.BooleanField(default=False, verbose_name='Номера для некурящих')),
                ('wifi', models.BooleanField(default=False, verbose_name='Wifi')),
                ('room_service', models.BooleanField(default=False, verbose_name='Доставка еды и напитков в номер')),
                ('coffee_teapot', models.BooleanField(default=False, verbose_name='Кофеварка/чайник')),
                ('bar', models.BooleanField(default=False, verbose_name='Бар')),
                ('city_view', models.BooleanField(default=False, verbose_name='Вид на город')),
                ('garden_view', models.BooleanField(default=False, verbose_name='Вид на сад')),
                ('outdoor_area', models.BooleanField(default=False, verbose_name='На свежем воздухе')),
                ('garden_furniture', models.BooleanField(default=False, verbose_name='Садовая мебель')),
                ('sun_terrace', models.BooleanField(default=False, verbose_name='Терасса для загара')),
                ('garden', models.BooleanField(default=False, verbose_name='Сад')),
                ('wine_champagne', models.BooleanField(default=False, verbose_name='Вино/шампанское')),
                ('kids_menu', models.BooleanField(default=False, verbose_name='Детское меню')),
                ('breakfast_in_room', models.BooleanField(default=False, verbose_name='Завтрак в номер')),
                ('restaurant', models.BooleanField(default=False, verbose_name='Archa Restaurant')),
                ('free_wifi', models.BooleanField(default=False, verbose_name='Бесплатный Wi-Fi на территории всего отеля')),
                ('daily_cleaning', models.BooleanField(default=False, verbose_name='Ежедневная уборка')),
                ('laundry_service', models.BooleanField(default=False, verbose_name='Услуги по глажению одежды')),
                ('paid_cleaning', models.BooleanField(default=False, verbose_name='Химчистка')),
                ('paid_laundry', models.BooleanField(default=False, verbose_name='Прачечная')),
                ('fax_xerox', models.BooleanField(default=False, verbose_name='Факс/ксерокопирование')),
                ('conference_banquet_hall', models.BooleanField(default=False, verbose_name='Конференц-зал/банкетный зал')),
                ('fire_extinguishers', models.BooleanField(default=False, verbose_name='Огнетушители')),
                ('smoke_detectors', models.BooleanField(default=False, verbose_name='Датчики дыма')),
                ('outdoor_surveillance', models.BooleanField(default=False, verbose_name='Видеонаблюдения снаружи здания')),
                ('public_areas_surveillance', models.BooleanField(default=False, verbose_name='Видеонаблюдения в местах общего пользования')),
                ('security_alarm', models.BooleanField(default=False, verbose_name='Охранная сигнализация')),
                ('full_time_security', models.BooleanField(default=False, verbose_name='Круглосуточная охрана')),
                ('safe', models.BooleanField(default=False, verbose_name='Сейф')),
                ('reception_desk', models.BooleanField(default=False, verbose_name='Стойка регистрации')),
                ('invoices_issued', models.BooleanField(default=False, verbose_name='Выдаются счета')),
                ('lockers', models.BooleanField(default=False, verbose_name='Запирающиеся шкафчики')),
                ('concierge_service', models.BooleanField(default=False, verbose_name='Услуги консьержа')),
                ('atm_on_site', models.BooleanField(default=False, verbose_name='Банкомат на территории отеля')),
                ('luggage_storage', models.BooleanField(default=False, verbose_name='Хранение багажа')),
                ('express_check_in', models.BooleanField(default=False, verbose_name='Ускоренная регистрация')),
                ('full_time_front_desk', models.BooleanField(default=False, verbose_name='Круглосуточная стойка регистрации')),
                ('minibar', models.BooleanField(default=False, verbose_name='Мини-бар')),
                ('terrace', models.BooleanField(default=False, verbose_name='Терраса')),
                ('balcony', models.BooleanField(default=False, verbose_name='Балкон')),
                ('patio', models.BooleanField(default=False, verbose_name='Патио')),
                ('fireplace', models.BooleanField(default=False, verbose_name='Камин')),
                ('garden_view_room', models.BooleanField(default=False, verbose_name='Вид на сад (в номере)')),
                ('city_view_room', models.BooleanField(default=False, verbose_name='Вид на город (в номере)')),
                ('tea_coffee_maker', models.BooleanField(default=False, verbose_name='Чайник/Кофемашина в номере')),
                ('housing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='housing_amenities', to='travel.housing')),
            ],
            options={
                'verbose_name': 'Удобства в объекте',
                'verbose_name_plural': 'Удобства в объекте',
            },
        ),
    ]
