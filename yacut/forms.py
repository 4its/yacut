from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (
    DataRequired, Length, Optional, Regexp, URL, ValidationError
)

from .models import URLMap
from settings import (
    FormText, TextErrors, SHORT_PATTERN, ORIGINAL_LENGTH, SHORT_LENGTH
)


class URLMapForm(FlaskForm):
    original_link = URLField(
        FormText.ORIGINAL_LABEL,
        validators=(
            DataRequired(message=FormText.REQUIRED_FIELD),
            Length(max=ORIGINAL_LENGTH),
            URL(require_tld=True, message=FormText.WRONG_ORIGINAL),
        )
    )
    custom_id = StringField(
        FormText.SHORT_LABEL,
        validators=(
            Optional(),
            Length(max=SHORT_LENGTH),
            Regexp(SHORT_PATTERN, message=FormText.WRONG_CHARS_IN_SHORT),
        )
    )
    submit = SubmitField(FormText.SUBMIT_LABEL)

    def validate_custom_id(self, custom_id):
        if URLMap.get(custom_id.data):
            raise ValidationError(TextErrors.SHORT_EXIST)
