# Generated by Django 4.2.3 on 2023-08-07 14:16

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_housing_image_alter_housing_food_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='image',
        ),
        migrations.AlterField(
            model_name='housing',
            name='housing_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('free_internet', 'Бесплатный интернет'), ('spa_services', 'Спа услуги'), ('restaurant', 'Ресторан'), ('Sports Hall', 'Спортивный зал'), ('pool', 'Бассейн'), ('airport_transfer', 'Трансфер от/до аэропорта'), ('fitness', 'Фитнес'), ('pet_allowed', 'Можно с питомцами'), ('indoor_pool', 'Крытый бассейн'), ('non_smoking_rooms', 'Номера для некурящих'), ('wifi', 'Wifi'), ('room_service', 'Доставка еды и напитков в номер'), ('coffee_teapot', 'Кофеварка/чайник'), ('bar', 'Бар'), ('garden_furniture', 'Садовая мебель'), ('sun_terrace', 'Терасса для загара'), ('garden', 'Сад'), ('wine_champagne', 'Вино/шампанское (платно)'), ('kids_menu', 'Детское меню (платно)'), ('breakfast_in_room', 'Завтрак в номер'), ('breakfast_paid', 'Завтрак включен в стоимость проживания?'), ('free_wifi', 'Бесплатный Wi-Fi на территории всего отеля'), ('daily_cleaning', 'Ежедневная уборка'), ('laundry_service', 'Услуги по глажению одежды (платно)'), ('paid_cleaning', 'Химчистка (платно)'), ('paid_laundry', 'Прачечная (платно)'), ('fax_xerox', 'Факс/ксерокопирование (платно)'), ('conference_banquet_hall', 'Конференц-зал/банкетный зал (платно)'), ('fire_extinguishers', 'Огнетушители'), ('smoke_detectors', 'Датчики дыма'), ('outdoor_surveillance', 'Видеонаблюдения снаружи здания'), ('public_areas_surveillance', 'Видеонаблюдения в местах общего пользования'), ('security_alarm', 'Охранная сигнализация'), ('full_time_security', 'Круглосуточная охрана'), ('safe', 'Сейф'), ('invoices_issued', 'Выдаются счета'), ('lockers', 'Запирающиеся шкафчики'), ('concierge_service', 'Услуги консьержа'), ('atm_on_site', 'Банкомат на территории отеля'), ('luggage_storage', 'Хранение багажа'), ('express_check_in', 'Ускоренная регистрация'), ('full_time_front_desk', 'Круглосуточная стойка регистрации'), ('transfer_paid', 'Трансфер (платно)'), ('food_delivery_to_room_paid', 'Доставка продуктов питания в номер (платно)'), ('smoking_areas', 'Места для курения'), ('air_conditioner', 'Кондиционер'), ('heating', 'Отопление'), ('car_rental', 'Прокат автомобилей'), ('packed_lunches', 'Упакованные ланчи'), ('ironing_facilities', 'Гладильные принадлежности'), ('buffet_breakfast', 'Завтрак "шведский стол"'), ('free_instant_coffee', 'Бесплатный растворимый кофе'), ('free_tea', 'Бесплатный чай'), ('happy_hour', 'Счастливый час'), ('special_diet_menu', 'Специальное диетическое меню'), ('taxi_service', 'Служба такси'), ('internet_business_center', 'Бизнес-центр с доступом в Интернет'), ('facial_treatments', 'Процедуры для лица'), ('foot_massage', 'Массаж ног'), ('full_body_massage', 'Массаж всего тела'), ('hammam', 'Хаммам'), ('manual_massage', 'Ручной массаж'), ('head_massage', 'Массаж головы'), ('massage', 'Массаж'), ('neck_massage', 'Массаж шеи'), ('steam_room', 'Паровая комната'), ('currency_exchange', 'Обмен валюты'), ('bell_staff_porter', 'Швейцар'), ('individual_check_in_check_out', 'Индивидуальная регистрация заезда/отъезда'), ('dry_cleaning', 'Сухая чистка'), ('shoe_shine', 'Чистка обуви'), ('kids_playground', 'Детская площадка'), ('allow_children', 'Можно c детьми'), ('allow_pets', 'C домашними животными'), ('pets_paid', 'Берете ли вы плату за домашних животных?'), ('Parking lot', 'Парковка')], max_length=1100, verbose_name='Удобства в объекте'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('air_conditioner', 'Кондиционер'), ('hair_dryer', 'Фен'), ('washing_machine', 'Стиральная машина'), ('iron', 'Утюг'), ('dryer', 'Сушильная машина'), ('fridge', 'Холодильник'), ('tv', 'Телевизор'), ('microwave', 'Микроволновка'), ('heating', 'Отопление'), ('sofa_bed', 'Диван-кровать'), ('folding_bed', 'Раскладная кровать'), ('Double bed', 'Двуспальная кровать'), ('wardrobe', 'Шкаф или гардероб'), ('linen', 'Белье'), ('clothes_hanger', 'Вешалка для одежды'), ('complimentary_toiletries', 'Бесплатные туалетно-косметические принадлежности'), ('toilet_paper', 'Туалетная бумага'), ('kitchen_utensils', 'Кухонные принадлежности'), ('electric_kettle', 'Электрический чайник'), ('city_view', 'Вид на город'), ('garden_view', 'Вид на сад'), ('high_toilet', 'Высокий туалет'), ('toilet_with_handles', 'Туалет с поручнями'), ('accessible_to_disabled_guests', 'Подходит для гостей с ограниченными возможностями'), ('work_desk', 'Рабочий стол'), ('room_cleaning', 'Уборка'), ('coffee_teapot', 'Кофеварка/чайник'), ('cable_satellite_tv', 'Кабельное / спутниковое телевидение'), ('bidet', 'Биде'), ('connecting_rooms_available', 'Доступны смежные номера'), ('room_service', 'Обслуживание номеров'), ('safe', 'Безопасный'), ('sitting_area', 'Зона отдыха'), ('telephone', 'Телефон'), ('bottled_water', 'Бутилированная вода'), ('Safe', 'Сейф'), ('laptop_safe_box', 'Сейф для ноутбука'), ('private_bathroom', 'Частные ванные комнаты'), ('wake_up_service', 'Услуга будильник / будильник'), ('minibar', 'Минибар'), ('flat_screen_tv', 'Телевизор с плоским экраном'), ('bath_or_shower', 'Ванна/душ'), ('Dressers', 'Комоды'), ('Mini kitchen', 'Мини кухня'), ('Fireplace', 'Камин'), ('Appetizers', 'Закуски'), ('2 rooms', '2 комнаты')], max_length=1100, verbose_name='Удобства номера'),
        ),
    ]
