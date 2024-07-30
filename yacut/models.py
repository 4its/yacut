from datetime import datetime
from random import choices
from re import match

from flask import url_for

from settings import (
    AVAILIBLE_CHARS, DEFAULT_SHORT_LENGTH, MAX_ATTEMPTS, ORIGINAL_LENGTH,
    SHORT_LENGTH, SHORT_PATTERN, REDIRECT_FUNCTION, TextErrors
)
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def short_link(self):
        return url_for(REDIRECT_FUNCTION, short=self.short, _external=True)

    def to_dict(self, original_only=False):
        if original_only:
            return dict(url=self.original)
        return dict(url=self.original, short_link=self.short_link())

    @staticmethod
    def get_object(short, or_404=False):
        if or_404:
            return URLMap.query.filter_by(short=short).first_or_404()
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def generate_short():
        for _ in range(MAX_ATTEMPTS):
            short = ''.join(choices(AVAILIBLE_CHARS, k=DEFAULT_SHORT_LENGTH))
            if not URLMap.get_object(short):
                return short
        raise RuntimeError(TextErrors.GENERATION_ERROR)

    @staticmethod
    def create_urlmap(original, short=None, from_form=False):
        if not short:
            short = URLMap.generate_short()
        if not from_form:
            if len(short) > SHORT_LENGTH or not match(SHORT_PATTERN, short):
                raise ValueError(TextErrors.BAD_CUSTOM_ID)
            if URLMap.get_object(short):
                raise ValueError(TextErrors.ID_ALREADY_EXIST)
            if len(original) > ORIGINAL_LENGTH:
                raise ValueError(TextErrors.BAD_ORIGINAL_LENGTH)
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
