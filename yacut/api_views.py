from re import match

from flask import jsonify, request

from . import app, db
from .constants import ID_PATTERN, TextErrors
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(TextErrors.NO_DATA_ERROR)
    if 'url' not in data:
        raise InvalidAPIUsage(TextErrors.NO_URL_ERROR)
    if 'custom_id' not in data or len(data['custom_id']) < 1:
        data['custom_id'] = get_unique_short_id()
    elif not match(ID_PATTERN, data['custom_id']):
        raise InvalidAPIUsage(TextErrors.BAD_CUSTOM_ID)
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(TextErrors.ID_ALREADY_EXIST)
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage(TextErrors.ID_NOT_FOUND, 404)
    return jsonify(dict(url=urlmap.original)), 200
