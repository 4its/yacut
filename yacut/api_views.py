from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from settings import TextErrors


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(TextErrors.NO_DATA_ERROR)
    if 'url' not in data:
        raise InvalidAPIUsage(TextErrors.NO_URL_ERROR)
    urlmap = URLMap.add_short(
        original=data['url'], short=data.get('custom_id')
    )
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.check_short(short_id)
    if url_map is None:
        raise InvalidAPIUsage(TextErrors.ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify(url_map.to_dict(True)), HTTPStatus.OK
