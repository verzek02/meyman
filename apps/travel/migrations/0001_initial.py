# Generated by Django 4.2.3 on 2023-08-18 17:41

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
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housing_name', models.CharField(max_length=255, verbose_name='Название места жительства')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('region', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область')),
                ('stars', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), (0, 'Без звезд')], default=1, verbose_name='Количество звезд')),
                ('housing_type', models.CharField(choices=[('Квартиры', 'Квартиры'), ('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Дома', 'Дома'), ('Санатории', 'Санатории')], max_length=50, verbose_name='Тип жилья')),
                ('accommodation_type', models.CharField(choices=[('Общая комната', 'Общая комната'), ('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната')], max_length=50, verbose_name='Тип размещения')),
                ('food_type', models.CharField(choices=[('Не включено', 'Не включено'), ('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=50, verbose_name='Тип питания')),
                ('housing_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('Бесплатный интернет', 'Бесплатный интернет'), ('Спа услуги', 'Спа услуги'), ('Ресторан', 'Ресторан'), ('Спортивный зал', 'Спортивный зал'), ('Бассейн', 'Бассейн'), ('Трансфер от/до аэропорта', 'Трансфер от/до аэропорта'), ('Фитнес', 'Фитнес'), ('Крытый бассейн', 'Крытый бассейн'), ('Номера для некурящих', 'Номера для некурящих'), ('Wifi', 'Wifi'), ('Доставка еды и напитков в номер', 'Доставка еды и напитков в номер'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Бар', 'Бар'), ('Садовая мебель', 'Садовая мебель'), ('Терасса для загара', 'Терасса для загара'), ('Сад', 'Сад'), ('Вино/шампанское (платно)', 'Вино/шампанское (платно)'), ('Детское меню (платно)', 'Детское меню (платно)'), ('Завтрак в номер', 'Завтрак в номер'), ('Завтрак включен в стоимость проживания?', 'Завтрак включен в стоимость проживания?'), ('Бесплатный Wi-Fi на территории всего отеля', 'Бесплатный Wi-Fi на территории всего отеля'), ('Ежедневная уборка', 'Ежедневная уборка'), ('Услуги по глажению одежды (платно)', 'Услуги по глажению одежды (платно)'), ('Химчистка (платно)', 'Химчистка (платно)'), ('Прачечная (платно)', 'Прачечная (платно)'), ('Факс/ксерокопирование (платно)', 'Факс/ксерокопирование (платно)'), ('Конференц-зал/банкетный зал (платно)', 'Конференц-зал/банкетный зал (платно)'), ('Огнетушители', 'Огнетушители'), ('Датчики дыма', 'Датчики дыма'), ('Видеонаблюдения снаружи здания', 'Видеонаблюдения снаружи здания'), ('Видеонаблюдения в местах общего пользования', 'Видеонаблюдения в местах общего пользования'), ('Охранная сигнализация', 'Охранная сигнализация'), ('Круглосуточная охрана', 'Круглосуточная охрана'), ('Сейф', 'Сейф'), ('Выдаются счета', 'Выдаются счета'), ('Запирающиеся шкафчики', 'Запирающиеся шкафчики'), ('Услуги консьержа', 'Услуги консьержа'), ('Банкомат на территории отеля', 'Банкомат на территории отеля'), ('Хранение багажа', 'Хранение багажа'), ('Ускоренная регистрация', 'Ускоренная регистрация'), ('Круглосуточная стойка регистрации', 'Круглосуточная стойка регистрации'), ('Трансфер (платно)', 'Трансфер (платно)'), ('Доставка продуктов питания в номер (платно)', 'Доставка продуктов питания в номер (платно)'), ('Места для курения', 'Места для курения'), ('Кондиционер', 'Кондиционер'), ('Отопление', 'Отопление'), ('Прокат автомобилей', 'Прокат автомобилей'), ('Упакованные ланчи', 'Упакованные ланчи'), ('Гладильные принадлежности', 'Гладильные принадлежности'), ('Завтрак "шведский стол"', 'Завтрак "шведский стол"'), ('Бесплатный растворимый кофе', 'Бесплатный растворимый кофе'), ('Бесплатный чай', 'Бесплатный чай'), ('Счастливый час', 'Счастливый час'), ('Специальное диетическое меню', 'Специальное диетическое меню'), ('Служба такси', 'Служба такси'), ('Бизнес-центр с доступом в Интернет', 'Бизнес-центр с доступом в Интернет'), ('Процедуры для лица', 'Процедуры для лица'), ('Массаж ног', 'Массаж ног'), ('Массаж всего тела', 'Массаж всего тела'), ('Хаммам', 'Хаммам'), ('Ручной массаж', 'Ручной массаж'), ('Массаж головы', 'Массаж головы'), ('Массаж', 'Массаж'), ('Массаж шеи', 'Массаж шеи'), ('Паровая комната', 'Паровая комната'), ('Обмен валюты', 'Обмен валюты'), ('Швейцар', 'Швейцар'), ('Индивидуальная регистрация заезда/отъезда', 'Индивидуальная регистрация заезда/отъезда'), ('Сухая чистка', 'Сухая чистка'), ('Чистка обуви', 'Чистка обуви'), ('Детская площадка', 'Детская площадка'), ('Можно c детьми', 'Можно c детьми'), ('C домашними животными', 'C домашними животными'), ('Берете ли вы плату за домашних животных?', 'Берете ли вы плату за домашних животных?'), ('Парковка', 'Парковка'), ('Джакузи', 'Джакузи'), ('Сауна', 'Сауна'), ('Камера хранения багажа', 'Камера хранения багажа'), ('Доступ людям с ограниченными возможностями', 'Доступ людям с ограниченными возможностями'), ('Сувенирный магазин', 'Сувенирный магазин'), ('Доступ в интернет: в номерах', 'Доступ в интернет: в номерах'), ('Доступ в интернет: на всей территории отеля', 'Доступ в интернет: на всей территории отеля'), ('Прокат автомобиля', 'Прокат автомобиля'), ('Питание', 'Питание'), ('Бар у бассейна', 'Бар у бассейна'), ('Кафе', 'Кафе')], max_length=1800, verbose_name='Удобства')),
                ('check_in_time_start', models.CharField(choices=[('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], max_length=5, verbose_name='Заезд С')),
                ('check_in_time_end', models.CharField(choices=[('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], max_length=5, verbose_name='Заезд До')),
                ('check_out_time_start', models.CharField(choices=[('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], max_length=5, verbose_name='Отъезд С')),
                ('check_out_time_end', models.CharField(choices=[('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], max_length=5, verbose_name='Отъезд До')),
                ('children_allowed', models.BooleanField(default=False, verbose_name='Можно ли проживать с детьми?')),
                ('pets_allowed', models.BooleanField(default=False, verbose_name='Можно ли проживать с домашними животными?')),
                ('pet_fee', models.BooleanField(default=False, verbose_name='Берете ли вы плату за домашних животных?')),
                ('breakfast_offered', models.BooleanField(default=False, verbose_name='Вы предлагаете гостям завтрак?')),
                ('breakfast_included', models.BooleanField(default=False, verbose_name='Завтрак включен в стоимость проживания?')),
                ('breakfast_cost_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Стоимость завтрака в US$ (с человека за ночь)')),
                ('breakfast_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Азиатский', 'Азиатский'), ('Континентальный', 'Континентальный'), ('Шведский', 'Шведский')], max_length=100, null=True, verbose_name='Какой тип завтрака вы предлагаете?')),
                ('parking', models.CharField(choices=[('Нет', 'Нет'), ('Да, бесплатно', 'Да, бесплатно'), ('Да, платно', 'Да, платно')], default='Нет', max_length=50, verbose_name='Услуги парковки')),
                ('parking_cost_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Стоимость парковки в US$ (за день)')),
                ('parking_location', models.CharField(blank=True, choices=[('На территории', 'На территории'), ('За территорией', 'За территорией')], max_length=50, null=True, verbose_name='Местонахождение парковки')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='человеко-понятный url')),
            ],
            options={
                'verbose_name': 'Место жительства',
                'verbose_name_plural': 'Места жительства',
            },
        ),
        migrations.CreateModel(
            name='HousingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='housing', verbose_name='Изображения мест жительств')),
            ],
            options={
                'verbose_name': 'Изображение места жительства',
                'verbose_name_plural': 'Изображения места жительств',
            },
        ),
        migrations.CreateModel(
            name='HousingReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 18))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 18))], verbose_name='Выезд')),
                ('adults', models.PositiveIntegerField(default=1, verbose_name='Взрослые(от 18 лет)')),
                ('teens', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Подростки(от 13-18 лет)')),
                ('children', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Дети(от 2-12 лет)')),
                ('infants', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Младенцы(младше 2)')),
                ('pets', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Домашние животные')),
            ],
            options={
                'verbose_name': 'Бронь жилья',
                'verbose_name_plural': 'Бронь жилищ',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(choices=[('Двухместный номер с 1 кроватью', 'Двухместный номер с 1 кроватью'), ('Двухместный с 2 отдельными кроватями', 'Двухместный с 2 отдельными кроватями'), ('Двухместный номер с 1 кроватью или 2 отдельными кроватями', 'Двухместный номер с 1 кроватью или 2 отдельными кроватями'), ('Люкс', 'Люкс'), ('Трехместный номер', 'Трехместный номер'), ('Семейный', 'Семейный'), ('Делюкс', 'Делюкс'), ('Четырехместный', 'Четырехместный'), ('Пентхаус', 'Пентхаус'), ('Коннектирующийся номер', 'Коннектирующийся номер'), ('Бизнес', 'Бизнес'), ('Королевский люкс', 'Королевский люкс'), ('Эконом', 'Эконом'), ('Стандартный', 'Стандартный')], max_length=100, verbose_name='название номера')),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена за ночь')),
                ('room_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('Кондиционер', 'Кондиционер'), ('Фен', 'Фен'), ('Стиральная машина', 'Стиральная машина'), ('Утюг', 'Утюг'), ('Сушильная машина', 'Сушильная машина'), ('Холодильник', 'Холодильник'), ('Телевизор', 'Телевизор'), ('Микроволновка', 'Микроволновка'), ('Отопление', 'Отопление'), ('Диван-кровать', 'Диван-кровать'), ('Раскладная кровать', 'Раскладная кровать'), ('Двуспальная кровать', 'Двуспальная кровать'), ('Шкаф или гардероб', 'Шкаф или гардероб'), ('Белье', 'Белье'), ('Вешалка для одежды', 'Вешалка для одежды'), ('Бесплатные туалетно-косметические принадлежности', 'Бесплатные туалетно-косметические принадлежности'), ('Туалетная бумага', 'Туалетная бумага'), ('Кухонные принадлежности', 'Кухонные принадлежности'), ('Электрический чайник', 'Электрический чайник'), ('Вид на город', 'Вид на город'), ('Вид на сад', 'Вид на сад'), ('Высокий туалет', 'Высокий туалет'), ('Туалет с поручнями', 'Туалет с поручнями'), ('Подходит для гостей с ограниченными возможностями', 'Подходит для гостей с ограниченными возможностями'), ('Рабочий стол', 'Рабочий стол'), ('Уборка', 'Уборка'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Кабельное / спутниковое телевидение', 'Кабельное / спутниковое телевидение'), ('Биде', 'Биде'), ('Доступны смежные номера', 'Доступны смежные номера'), ('Обслуживание номеров', 'Обслуживание номеров'), ('Безопасный', 'Безопасный'), ('Зона отдыха', 'Зона отдыха'), ('Телефон', 'Телефон'), ('Бутилированная вода', 'Бутилированная вода'), ('Сейф', 'Сейф'), ('Сейф для ноутбука', 'Сейф для ноутбука'), ('Частные ванные комнаты', 'Частные ванные комнаты'), ('Услуга будильник / будильник', 'Услуга будильник / будильник'), ('Минибар', 'Минибар'), ('Ванна/душ', 'Ванна/душ'), ('Комоды', 'Комоды'), ('Мини кухня', 'Мини кухня'), ('Камин', 'Камин'), ('Закуски', 'Закуски'), ('2 комнаты', '2 комнаты'), ('Тумба', 'Тумба'), ('Телевизор', 'Телевизор'), ('Ванная комната', 'Ванная комната'), ('Телефон', 'Телефон'), ('Комоды', 'Комоды'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат')], max_length=850, verbose_name='Удобства')),
                ('num_rooms', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Количество комнат в номере')),
                ('bedrooms', models.CharField(choices=[('1 спальня', '1 спальня'), ('2 спальни', '2 спальни'), ('Больше 3 спален', 'Больше 3 спален')], max_length=50, verbose_name='Количество спален')),
                ('bed_type', models.CharField(choices=[('Односпальные', 'Односпальные'), ('Двуспальная', 'Двуспальная'), ('Kingsize', 'Kingsize'), ('Queensize', 'Queensize'), ('Диван-кровать', 'Диван-кровать')], max_length=50, verbose_name='Тип кроватей')),
                ('single_bed', models.PositiveIntegerField(default=1, verbose_name='Односпальных кроватей')),
                ('double_bed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Двуспальных кроватей')),
                ('queen_bed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Широких (queen-size) кроватей')),
                ('king_bed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Широких (king-size) кроватей')),
                ('sofa_bed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Диван-кроватей')),
                ('max_guest_capacity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Максимальная вместимость гостей в номере')),
                ('room_area', models.PositiveIntegerField(verbose_name='Площадь комнаты(м²)')),
                ('smoking_allowed', models.BooleanField(default=False, verbose_name='Разрешено ли курение в комнате')),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='travel.housing', verbose_name='Название места жительства')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
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
            name='House',
            fields=[
                ('housing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travel.housing')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
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
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='rooms', verbose_name='Изображения номера')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='travel.room')),
            ],
            options={
                'verbose_name': 'Изображение номера',
                'verbose_name_plural': 'Изображения номеров',
            },
        ),
        migrations.CreateModel(
            name='HousingReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('cleanliness_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Чистота')),
                ('comfort_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Комфорт')),
                ('staff_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Персонал')),
                ('value_for_money_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Цена/Качества')),
                ('food_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Питание')),
                ('location_rating', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Местоположение')),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='travel.housing', verbose_name='Название места жительства')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
