import os
from re import escape
from string import ascii_letters, digits


REDIRECT_FUNCTION = 'redirect_to'

# Models default values.
ORIGINAL_LENGTH = 2048
SHORT_LENGTH = 16

# Custom ID generator parameters
MAX_ATTEMPTS = 10
DEFAULT_SHORT_LENGTH = 6
AVAILIBLE_CHARS = ascii_letters + digits
SHORT_PATTERN = f'^[{escape(AVAILIBLE_CHARS)}]*$'


class Config(object):
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


class FormText:
    REQUIRED_FIELD = 'Обязательное поле'
    ORIGINAL_LABEL = 'Длинная ссылка'
    WRONG_ORIGINAL = 'Неправильная ссылка'
    SHORT_LABEL = 'Ваш вариант короткой ссылки'
    WRONG_CHARS_IN_SHORT = 'Недопустимые символы в короткой ссылке'
    SUBMIT_LABEL = 'Создать'


class TextErrors:
    NO_DATA_ERROR = 'Отсутствует тело запроса'
    NO_URL_ERROR = '"url" является обязательным полем!'
    BAD_SHORT = 'Указано недопустимое имя для короткой ссылки'
    SHORT_EXIST = 'Предложенный вариант короткой ссылки уже существует.'
    SHORT_NOT_FOUND = 'Указанный id не найден'
    GENERATION_ERROR = (
        f'Не удалось сгенерировать короткую ссылку за {MAX_ATTEMPTS} попыток.'
    )
    BAD_ORIGINAL_LENGTH = (
        f'Длинна оригинальной ссылки превышает {ORIGINAL_LENGTH} символов'
    )
