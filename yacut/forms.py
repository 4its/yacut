from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Оригинальная ссылка',
        validators=(
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        )
    )
    custom_id = StringField(
        'Пользовательские идентификатор',
        validators=(
            Optional,
            Length(1, 16)
        )
    )
    submit = SubmitField('Создать')
