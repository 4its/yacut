from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import (
    FormText, ID_PATTERN, ORIGINAL_URL_LENGTH, SHORT_URL_LENGTH
)


class URLMapForm(FlaskForm):
    original_link = URLField(
        FormText.LINK_LABEL,
        validators=(
            DataRequired(message=FormText.REQUIRED_FIELD),
            Length(max=ORIGINAL_URL_LENGTH),
            URL(require_tld=True, message=FormText.WRONG_URL),
        )
    )
    custom_id = StringField(
        FormText.ID_LABEL,
        validators=(
            Optional(),
            Length(max=SHORT_URL_LENGTH),
            Regexp(ID_PATTERN, message=FormText.WRONG_CHARS),
        )
    )
    submit = SubmitField(FormText.SUBMIT_LABEL)
