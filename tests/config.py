import string
class Config:
    BASE_URL = 'https://b2c.passport.rt.ru/' #страница авторизации
    BASE_REG_URL = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'

    VALID_EMAIL = "zobyhh@gmail.com"
    VALID_PHONE = "+79667858499"
    INVALID_PHONE = "+79667431614"
    VALID_PASSWORD = "Zq159753"
    INVALID_EMAIL = "Test@gmail.com"
    INVALID_PASSWORD = "InvalidPass123"
    REQ_ELEMENTS_AUTH = ["Авторизация", "Телефон", "Почта", "Логин", "Лицевой счёт"]
    REQ_ELEMENTS_RESET = ["Телефон", "Почта", "Логин", "Лицевой счёт"]
    DEFAULT_LOGIN_TEXT = "Мобильный телефон"
    TAGLINE_TEXT = "Персональный помощник в цифровом мире Ростелекома"

    FIRSTNAME = "Арам"
    LASTNAME = "Арутюнов"
    NEW_EMAIL = 'yahanig853@ahieh.com'
    NEW_PASSWORD = "NewPass123"

def generate_string_rus(n):
    return 'б' * n

def generate_string_en(n):
    return 'x' * n

def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'

def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'

def chinese_chars():  # 20 популярных китайских иероглифов
    return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
    return f'{string.punctuation}'