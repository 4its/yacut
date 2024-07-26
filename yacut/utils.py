from random import choices
from string import ascii_letters, digits


AVAILIBLE_CHARS = ascii_letters + digits
DEFAULT_LENGTH = 6


def get_unique_short_id():
    return ''.join(choices(AVAILIBLE_CHARS, k=DEFAULT_LENGTH))
