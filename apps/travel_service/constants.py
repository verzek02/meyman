DESTINATION_CHOICES = (
    ('Бишкек', 'Бишкек'),
    ('Джалал-Абад', 'Джалал-Абад'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Ош', 'Ош'),
    ('Нарын', 'Нарын'),
    ('Талас', 'Талас'),
    ('Баткен', 'Баткен'),
)

CAR_CATEGORIES = (
    ('Легковушка', 'Легковушка'),
    ('Минивэн', 'Минивэн'),
    ('Внедорожник', 'Внедорожник'),
    ('Автобус', 'Автобус'),
    ('Кроссовер', 'Кроссовер'),
)

BRAND_CHOICES = (
    ('Мерседес-бенц', 'Мерседес-бенц'),
    ('Лендровер', 'Лендровер'),
    ('БМВ', 'БМВ'),
    ('Вольво', 'Вольво'),
    ('Шевролед', 'Шевролед'),
    ('Фольксваген', 'Фольксваген'),
    ('Хонда', 'Хонда'),
    ('Ауди', 'Ауди'),
    ('Хендай', 'Хендай'),
    ('Форд', 'Форд'),
    ('Киа', 'Киа'),
    ('Лексус', 'Лексус'),
    ('Мицубиси', 'Мицубиси'),
    ('Рено', 'Рено'),
    ('Опель', 'Опель'),
    ('Субару', 'Субару'),
    ('Мазда', 'Мазда'),
    ('Порше', 'Порше'),
    ('Дэу', 'Дэу'),
    ('Лада', 'Лада'),
    ('Сузуки', 'Сузуки'),
    ('Инфинити', 'Инфинити'),
    ('Ссанг Йонг', 'Ссанг Йонг'),
    ('Ниссан', 'Ниссан'),
    ('Тойота', 'Тойота'),
)

TRANSMISSION_TYPES = (
    ('Механическая', 'Механическая'),
    ('Автоматическая', 'Автоматическая'),
    ('Другое', 'Другое'),
)

STEERING_TYPES = (
    ('Левый', 'Левый'),
    ('Правый', 'Правый'),
)

BODY_TYPES = (
    ('Седан', 'Седан'),
    ('Купе', 'Купе'),
    ('Хэтчбек', 'Хэтчбек'),
    ('Лифтбек', 'Лифтбек'),
    ('Фастбэк', 'Фастбэк'),
    ('Универсал', 'Универсал'),
    ('Кроссовер', 'Кроссовер'),
    ('Внедорожник', 'Внедорожник'),
    ('Легковой фургон', 'Легковой фургон'),
    ('Минивэн', 'Минивэн'),
    ('Компактвэн', 'Компактвэн'),
    ('Микровэн', 'Микровэн'),
    ('Кабриолет', 'Кабриолет'),
    ('Родстер', 'Родстер'),
    ('Тарга', 'Тарга'),
    ('Ландо', 'Ландо'),
    ('Лимузин', 'Лимузин'),
)

DRIVE_TYPES = (
    ('Передний', 'Передний'),
    ('Задний', 'Задний'),
    ('Полный', 'Полный'),
)

FUEL_TYPES = (
    ('Бензин', 'Бензин'),
    ('Бензин/Газ', 'Бензин/Газ'),
    ('Газ', 'Газ'),
    ('Дизель', 'Дизель'),
    ('Электрический', 'Электрический'),
    ('Другое', 'Другое'),
)

SEATING_CAPACITY = (
    ('2', '2 пассажира'),
    ('5', '5 пассажиров'),
    ('8', '8 пассажиров'),
    ('Другое', 'Другое'),
)

CONDITION_CHOICES = (
    ('Хорошее', 'Хорошее'),
    ('Идеальное', 'Идеальное'),
    ('Новое', 'Новое'),
)

MINIMUM_AGE_CHOICES = (
    ('18', '18 лет'),
    ('20', '20 лет'),
    ('22', '22 года'),
    ('24', '24 года'),
    ('26', '26 лет'),
    ('28', '28 лет'),
    ('30', '30 лет'),
    ('32', '32 года'),
    ('34', '34 года'),
    ('36', '36 лет'),
    ('38', '38 лет'),
    ('40', '40 лет'),
    ('42', '42 года'),
    ('44', '44 года'),
    ('46', '46 лет'),
    ('48', '48 лет'),
    ('50', '50 лет'),
)

CURRENCY_CHOICES = (
    ('Рубль', 'Рубль'),
    ('Сом', 'Сом'),
    ('USD', 'USD'),
)


SAFETY_EQUIPMENT_CHOICES = [
    ('fire_extinguisher', 'Наличие огнетушителя'),
    ('first_aid_kit', 'Наличие аптечки'),
    ('spare_wheel', 'Наличие запасного колеса'),
    ('airbags', 'Наличие подушка безопасности'),
    ('emergency_tools', 'Наличие инструментов аварийной ситуации'),
    ('dashboard_camera', 'Наличие авторегистратора'),
]

COLOR_CHOICES = (
    ('Серебристый', 'Серебристый'),
    ('Черный', 'Черный'),
    ('Белый', 'Белый'),
    ('Серый', 'Серый'),
    ('Бежевый', 'Бежевый'),
    ('Бирюзовый', 'Бирюзовый'),
    ('Бордовый', 'Бордовый'),
    ('Бронза', 'Бронза'),
    ('Хамелеон', 'Хамелеон'),
    ('Жёлтый', 'Жёлтый'),
    ('Зеленый', 'Зеленый'),
    ('Золотоый', 'Золотоый'),
    ('Коричневый', 'Коричневый'),
    ('Фиолетовый', 'Фиолетовый'),
    ('Синий', 'Синий'),
    ('Красный', 'Красный'),
    ('Оранжевый', 'Оранжевый'),
    ('Розовый', 'Розовый'),
    ('Сиреневый', 'Сиреневый'),
    ('Вишьня', 'Вишьня'),
    ('Баклажан', 'Баклажан'),
    ('Голубой', 'Голубой'),
)

YES_OR_NO = (
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)