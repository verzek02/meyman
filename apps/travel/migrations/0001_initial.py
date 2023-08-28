# Generated by Django 4.2.3 on 2023-08-28 15:50

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
                ('region', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область')),
                ('stars', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), (0, 'Без звезд')], default=1, verbose_name='Количество звезд')),
                ('housing_type', models.CharField(choices=[('Квартиры', 'Квартиры'), ('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Дома', 'Дома'), ('Санатории', 'Санатории')], max_length=50, verbose_name='Тип жилья')),
                ('accommodation_type', models.CharField(choices=[('Общая комната', 'Общая комната'), ('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната')], max_length=50, verbose_name='Тип размещения')),
                ('food_type', models.CharField(choices=[('Не включено', 'Не включено'), ('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=50, verbose_name='Тип питания')),
                ('free_internet', models.BooleanField(default=False, verbose_name='Бесплатный интернет')),
                ('restaurant', models.BooleanField(default=False, verbose_name='Ресторан')),
                ('airport_transfer', models.BooleanField(default=False, verbose_name='Трансфер от/до аэропорта')),
                ('paid_transfer', models.BooleanField(default=False, verbose_name='Платно за трансфер')),
                ('gym', models.BooleanField(default=False, verbose_name='Спортивный зал')),
                ('children_playground', models.BooleanField(default=False, verbose_name='Детская площадка')),
                ('car_rental', models.BooleanField(default=False, verbose_name='Прокат автомобиля')),
                ('park', models.BooleanField(default=False, verbose_name='Парковка')),
                ('paid_parking', models.BooleanField(default=False, verbose_name='Платно за парковку')),
                ('spa_services', models.BooleanField(default=False, verbose_name='Спа услуги')),
                ('bar', models.BooleanField(default=False, verbose_name='Бар')),
                ('paid_bar', models.BooleanField(default=False, verbose_name='Платно за бар')),
                ('pool', models.BooleanField(default=False, verbose_name='Бассейн')),
                ('room_service', models.BooleanField(default=False, verbose_name='Обслуживание номеров')),
                ('poolside_bar', models.BooleanField(default=False, verbose_name='Бар у бассейна')),
                ('cafe', models.BooleanField(default=False, verbose_name='Кафе')),
                ('in_room_internet', models.BooleanField(default=False, verbose_name='Доступ в интернет: в номерах')),
                ('hotel_wide_internet', models.BooleanField(default=False, verbose_name='Доступ в интернет: на всей территории отеля')),
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
                ('parking_location', models.CharField(blank=True, choices=[('На территории', 'На территории'), ('За территорией', 'За территорией')], max_length=50, null=True, verbose_name='Местонахождение парковки')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='человеко-понятный url')),
            ],
            options={
                'verbose_name': 'Место жительства',
                'verbose_name_plural': 'Места жительства',
            },
        ),
        migrations.CreateModel(
            name='HousingAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Календарь',
                'verbose_name_plural': 'Календари',
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
                ('destination', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 28))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 28))], verbose_name='Выезд')),
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
                ('room_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('Двуспальная кровать', 'Двуспальная кровать'), ('Кондиционер', 'Кондиционер'), ('Тумба', 'Тумба'), ('Телевизор', 'Телевизор'), ('Стиральная машина', 'Стиральная машина'), ('Ванная комната', 'Ванная комната'), ('Утюг', 'Утюг'), ('2 комнаты', '2 комнаты'), ('Холодильник', 'Холодильник'), ('Фен', 'Фен'), ('Сейф', 'Сейф'), ('Телефон', 'Телефон'), ('Комоды', 'Комоды'), ('Шкафы', 'Шкафы'), ('Мини кухня', 'Мини кухня'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат'), ('Закуски', 'Закуски'), ('Камин', 'Камин')], max_length=255, verbose_name='Удобства')),
                ('kitchen', multiselectfield.db.fields.MultiSelectField(choices=[('чайник', 'Электронный чайник'), ('микроволновка', 'Микроволновка'), ('обеденный_стол', 'Обеденный стол'), ('кофеварка', 'Кофеварка'), ('mini_bar', 'Mini-bar'), ('холодильник', 'Холодильник')], max_length=255, verbose_name='Кухня')),
                ('outside', multiselectfield.db.fields.MultiSelectField(choices=[('Балкон', 'Балкон'), ('Терраса', 'Терраса'), ('Вид из окна', 'Вид из окна')], max_length=255, verbose_name='На улице')),
                ('bathroom', multiselectfield.db.fields.MultiSelectField(choices=[('Душ', 'Душ'), ('Туалетная бумага', 'Туалетная бумага'), ('Туалет', 'Туалет'), ('Фен', 'Фен'), ('Ванна', 'Ванна'), ('Бесплатные уходовые средства', 'Бесплатные уходовые средства'), ('Биде', 'Биде'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат')], max_length=255, verbose_name='Ванная')),
                ('num_rooms', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Количество комнат в номере')),
                ('bedrooms', models.CharField(choices=[('1 спальня', '1 спальня'), ('2 спальни', '2 спальни'), ('Больше 3 спален', 'Больше 3 спален')], max_length=50, verbose_name='Количество спален')),
                ('bed_type', multiselectfield.db.fields.MultiSelectField(choices=[('Односпальные', 'Односпальные'), ('Двуспальная', 'Двуспальная'), ('Kingsize', 'Kingsize'), ('Queensize', 'Queensize'), ('Диван-кровать', 'Диван-кровать')], max_length=100, verbose_name='Тип кроватей')),
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
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rooms', verbose_name='Изображения номера')),
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
