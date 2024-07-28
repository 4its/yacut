from datetime import datetime
from random import choices
from re import match

from flask import url_for

from settings import (
    AVAILIBLE_CHARS, DEFAULT_LENGTH, ORIGINAL_LENGTH,
    SHORT_LENGTH, SHORT_PATTERN, REDIRECT_FUNCTION, TextErrors
)
from yacut import db
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def short_link(self):
        return url_for(REDIRECT_FUNCTION, short=self.short, _external=True)

    def to_dict(self, short=False):
        if short:
            return dict(url=self.original)
        return dict(url=self.original, short_link=self.short_link())

    @staticmethod
    def check_short(short, or_404=False):
        if not or_404:
            return URLMap.query.filter_by(short=short).first()
        return URLMap.query.filter_by(short=short).first_or_404()

    @staticmethod
    def generate_short():
        while True:
            short = ''.join(choices(AVAILIBLE_CHARS, k=DEFAULT_LENGTH))
            if not URLMap.check_short(short):
                return short

    @staticmethod
    def add_short(original, short=None):
        if short is None:
            short = URLMap.generate_short()
        elif URLMap.check_short(short):
            raise InvalidAPIUsage(TextErrors.LABEL_EXIST)
        elif not match(SHORT_PATTERN, short) or len(short) > SHORT_LENGTH:
            raise InvalidAPIUsage(TextErrors.BAD_CUSTOM_ID)
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
