from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

REQUIRED_FIELD = 'Обязательное поле'
WRONG_URL = 'Неправильный URL'
LINK_LABEL = 'Длинная ссылка'
ID_LABEL = 'Ваш вариант короткой ссылки'
WRONG_CHARS = 'Недопустимые символы в короткой ссылке'
SUBMIT_LABEL = 'Создать'
CUSTOM_ID_PATTERN = r'^[A-Za-z0-9]+$'


class URLMapForm(FlaskForm):
    original_link = URLField(
        LINK_LABEL,
        validators=(
            DataRequired(message=REQUIRED_FIELD),
            Length(1, 256),
            URL(require_tld=True, message=WRONG_URL),
        )
    )
    custom_id = StringField(
        ID_LABEL,
        validators=(
            Length(1, 16),
            Optional(),
            Regexp(CUSTOM_ID_PATTERN, message=WRONG_CHARS),
        )
    )
    submit = SubmitField(SUBMIT_LABEL)
