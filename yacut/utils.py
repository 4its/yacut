from random import choices

from .constants import AVAILIBLE_CHARS, DEFAULT_LENGTH
from .models import URLMap


def get_unique_short_id():
    while True:
        short_id = ''.join(choices(AVAILIBLE_CHARS, k=DEFAULT_LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
