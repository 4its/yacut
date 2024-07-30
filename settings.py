import os
from re import escape
from string import ascii_letters, digits


REDIRECT_FUNCTION = 'redirect_to'

# Models default values.
ORIGINAL_LENGTH = 512
SHORT_LENGTH = 16

# Custom ID generator parameters
MAX_ATTEMPTS = 10
DEFAULT_SHORT_LENGTH = 6
AVAILIBLE_CHARS = ascii_letters + digits
ESCAPED_AVAILABLE_CHARS = escape(AVAILIBLE_CHARS)
SHORT_PATTERN = f'^[{ESCAPED_AVAILABLE_CHARS}]*$'


class Config(object):
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


class FormText:
    REQUIRED_FIELD = 'Обязательное поле'
    WRONG_URL = 'Неправильный URL'
    LINK_LABEL = 'Длинная ссылка'
    ID_LABEL = 'Ваш вариант короткой ссылки'
    WRONG_CHARS = 'Недопустимые символы в короткой ссылке'
    SUBMIT_LABEL = 'Создать'


class TextErrors:
    NO_DATA_ERROR = 'Отсутствует тело запроса'
    NO_URL_ERROR = '"url" является обязательным полем!'
    BAD_CUSTOM_ID = 'Указано недопустимое имя для короткой ссылки'
    ID_ALREADY_EXIST = 'Предложенный вариант короткой ссылки уже существует.'
    ID_NOT_FOUND = 'Указанный id не найден'
    LABEL_EXIST = 'Предложенный вариант короткой ссылки уже существует.'
    GENERATION_ERROR = 'Не удалось сгенерировать короткую ссылку.'
    BAD_ORIGINAL_LENGTH = (
        f'Длинна оригинальной ссылки превышает {ORIGINAL_LENGTH} символов'
    )
