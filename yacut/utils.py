from random import choices

from settings import AVAILIBLE_CHARS, DEFAULT_LENGTH
from .models import URLMap


def get_unique_short_id():
    while True:
        short = ''.join(choices(AVAILIBLE_CHARS, k=DEFAULT_LENGTH))
        if not URLMap.query.filter_by(short=short).first():
            return short
