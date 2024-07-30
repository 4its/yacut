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
    try:
        return jsonify(
            URLMap.create_urlmap(
                original=data['url'], short=data.get('custom_id')
            ).to_dict()
        ), HTTPStatus.CREATED
    except (RuntimeError, ValueError) as error:
        raise InvalidAPIUsage(str(error))


@app.route('/api/id/<short>/', methods=['GET'])
def get_url(short):
    url_map = URLMap.get_object(short)
    if url_map is None:
        raise InvalidAPIUsage(TextErrors.SHORT_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify(url_map.to_dict(True)), HTTPStatus.OK
