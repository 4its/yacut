from datetime import datetime

from flask import url_for

from settings import ORIGINAL_URL_LENGTH, SHORT_URL_LENGTH
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_URL_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_URL_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_to', short=self.short, _external=True)
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
