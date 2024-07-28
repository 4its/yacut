import os
from string import ascii_letters, digits


# Models default values.
ORIGINAL_URL_LENGTH = 256
SHORT_URL_LENGTH = 16

# for Custom ID generator
AVAILIBLE_CHARS = ascii_letters + digits
DEFAULT_LENGTH = 6
ID_PATTERN = r'^[A-Za-z0-9]{1,%d}$' % SHORT_URL_LENGTH


class Config(object):
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


class FormText:
    """Texts used in Forms."""
    REQUIRED_FIELD = 'Обязательное поле'
    WRONG_URL = 'Неправильный URL'
    LINK_LABEL = 'Длинная ссылка'
    ID_LABEL = 'Ваш вариант короткой ссылки'
    WRONG_CHARS = 'Недопустимые символы в короткой ссылке'
    SUBMIT_LABEL = 'Создать'


class TextErrors:
    """Texts used for error messages."""
    NO_DATA_ERROR = 'Отсутствует тело запроса'
    NO_URL_ERROR = '"url" является обязательным полем!'
    BAD_CUSTOM_ID = 'Указано недопустимое имя для короткой ссылки'
    ID_ALREADY_EXIST = 'Предложенный вариант короткой ссылки уже существует.'
    ID_NOT_FOUND = 'Указанный id не найден'
    LABEL_EXIST = 'Предложенный вариант короткой ссылки уже существует.'