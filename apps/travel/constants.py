HOUSING_CHOICES = (
    ('Квартиры', 'Квартиры'),
    ('Отели', 'Отели'),
    ('Хостелы', 'Хостелы'),
    ('Дома', 'Дома'),
    ('Санатории', 'Санатории'),
)

ACCOMMODATION_CHOICES = (
    ("Общая комната", "Общая комната"),
    ("Жилье целиком", "Жилье целиком"),
    ("Комната", "Комната"),
)

BEDROOM_CHOICES = (
    ("1 спальня", "1 спальня"),
    ("2 спальни", "2 спальни"),
    ("Больше 3 спален", "Больше 3 спален"),
)

BED_CHOICES = (
    ("Односпальные", "Односпальные"),
    ("Двуспальная", "Двуспальная"),
    ("Kingsize", "Kingsize"),
    ("Queensize", "Queensize"),
    ("Диван-кровать", "Диван-кровать"),
)

FOOD_CHOICES = (
    ("Не включено", "Не включено"),
    ("Все включено", "Все включено"),
    ("Завтрак включен", "Завтрак включен"),
    ("С собственной кухней", "С собственной кухней"),
)

PARKING_LOCATION_CHOICES = (
    ('На территории', 'На территории'),
    ('За территорией', 'За территорией'),
)

HOUSING_AMENITIES_CHOICES = (
    ('Бесплатный интернет', 'Бесплатный интернет'),
    ('Спа услуги', 'Спа услуги'),
    ('Трансфер от/до аэропорта - Платно', 'Трансфер от/до аэропорта'),
    ('Парковка- Платно', 'Парковка'),
    ('Бар- Платно', 'Бар'),
    ('Химчистка- Платно', 'Химчистка'),
    ('Прачечная- Платно', 'Прачечная'),
    ('Камера хранения багажа', 'Камера хранения багажа'),
    ('Круглосуточная стойка регистрации', 'Круглосуточная стойка регистрации'),
    ('Доступ людям с ограниченными возможностями', 'Доступ людям с ограниченными возможностями'),
    ('Бар у бассейна- Платно', 'Бар у бассейна'),
    ('Кафе- Платно', 'Кафе'),
    ('Массаж', 'Массаж'),
    ('Джакузи', 'Джакузи'),
    ('Сауна', 'Сауна'),
    ('Хаммам', 'Хаммам'),
    ('Спортивный зал', 'Спортивный зал'),
    ('Доступ в интернет:в номерах', 'Доступ в интернет:в номерах'),
    ('Доступ в интернет:на всей территории отеля', 'Доступ в интернет:на всей территории отеля')
)
KITCHEN_CHOICES = (
    ('чайник', 'Электронный чайник'),
    ('микроволновка', 'Микроволновка'),
    ('обеденный_стол', 'Обеденный стол'),
    ('кофеварка', 'Кофеварка'),
    ('mini_bar', 'Mini-bar'),
    ('холодильник', 'Холодильник'),
)

OUTSIDE_CHOICES = (
    ('Балкон', 'Балкон'),
    ('Терраса', 'Терраса'),
    ('Вид из окна', 'Вид из окна'),
)

ROOM_AMENITIES_CHOICES = (
    ('Двуспальная кровать', 'Двуспальная кровать'),
    ('Кондиционер', 'Кондиционер'),
    ('Тумба', 'Тумба'),
    ('Телевизор', 'Телевизор'),
    ('Стиральная машина', 'Стиральная машина'),
    ('Ванная комната', 'Ванная комната'),
    ('Утюг', 'Утюг'),
    ('2 комнаты', '2 комнаты'),
    ('Холодильник', 'Холодильник'),
    ('Фен', 'Фен'),
    ('Сейф', 'Сейф'),
    ('Телефон', 'Телефон'),
    ('Комоды', 'Комоды'),
    ('Шкафы', 'Шкафы'),
    ('Мини кухня', 'Мини кухня'),
    ('Тапочки', 'Тапочки'),
    ('Халат', 'Халат'),
    ('Закуски', 'Закуски'),
    ('Камин', 'Камин'),
)

BATHROOM_AMENITIES_CHOICES = [
    ('Душ', 'Душ'),
    ('Туалетная бумага', 'Туалетная бумага'),
    ('Туалет', 'Туалет'),
    ('Фен', 'Фен'),
    ('Ванна', 'Ванна'),
    ('Бесплатные уходовые средства', 'Бесплатные уходовые средства'),
    ('Биде', 'Биде'),
    ('Тапочки', 'Тапочки'),
    ('Халат', 'Халат'),
]

ACCOMMODATION_TYPE_CHOICES = (
    ('Двухместный номер с 1 кроватью', 'Двухместный номер с 1 кроватью'),
    ('Двухместный с 2 отдельными кроватями', 'Двухместный с 2 отдельными кроватями'),
    ('Двухместный номер с 1 кроватью или 2 отдельными кроватями',
     'Двухместный номер с 1 кроватью или 2 отдельными кроватями'),
    ('Люкс', 'Люкс'),
    ('Трехместный номер', 'Трехместный номер'),
    ('Семейный', 'Семейный'),
    ('Делюкс', 'Делюкс'),
    ('Четырехместный', 'Четырехместный'),
    ('Пентхаус', 'Пентхаус'),
    ('Коннектирующийся номер', 'Коннектирующийся номер'),
    ('Бизнес', 'Бизнес'),
    ('Королевский люкс', 'Королевский люкс'),
    ('Эконом', 'Эконом'),
    ('Стандартный', 'Стандартный'),
)

TIME_CHOICES = [(f'{hour:02d}:00', f'{hour:02d}:00') for hour in range(24)]

BREAKFAST_CHOICES = (
    ('Азиатский', 'Азиатский'),
    ('Континентальный', 'Континентальный'),
    ('Шведский', 'Шведский'),
)

STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    (0, 'Без звезд'),
)

RATING_CHOICES = (
    (10, "Замечательно"),
    (9, "Превосходно"),
    (8, "Очень хорошо"),
    (7, "Хорошо"),
    (6, "Достаточно хорошо"),
    (5, "Нормально"),
    (4, "Неудовлетворительно"),
    (3, "Плохо"),
    (2, "Очень плохо"),
    (1, "Ужасно"),
)

RATING_RANGE_CHOICES = (
    ("9-10", "9-10"),
    ("8-9", "8-9"),
    ("7-8", "7-8"),
    ("5-7", "5-7"),
)
