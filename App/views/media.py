from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_media,
    get_media,
    get_all_media_json,
    get_tag_eventID,
)

media_views = Blueprint('media_views', __name__, template_folder='../templates')

@media_views.route('/api/media', methods=['GET'])
def get_media_action():
     all_media = get_all_media_json()
     return jsonify(all_media)
    #pass

@media_views.route('/api/media', methods=['POST'])
def create_media_action():
    data = request.json
    res = create_media(data['tagEventId'], data['filename'], data['url'])
    if res: 
        return jsonify({'message': f"media {data['filename']} created"}), 201
    return jsonify({'message': f"error creating media"}), 401
