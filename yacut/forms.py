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
        FormText.LINK_LABEL,
        validators=(
            DataRequired(message=FormText.REQUIRED_FIELD),
            Length(max=ORIGINAL_LENGTH),
            URL(require_tld=True, message=FormText.WRONG_URL),
        )
    )
    custom_id = StringField(
        FormText.ID_LABEL,
        validators=(
            Optional(),
            Length(max=SHORT_LENGTH),
            Regexp(SHORT_PATTERN, message=FormText.WRONG_CHARS),
        )
    )
    submit = SubmitField(FormText.SUBMIT_LABEL)

    def validate_custom_id(self, custom_id):
        if not custom_id.data and URLMap.check_short(custom_id.data):
            raise ValidationError(TextErrors.LABEL_EXIST)
