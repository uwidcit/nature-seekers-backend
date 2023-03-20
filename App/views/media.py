from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_media,
    get_media,
    get_all_media_json,
    delete_media
)

media_views = Blueprint('media_views', __name__, template_folder='../templates')

@media_views.route('/api/media', methods=['GET'])
def get_media_action():
     all_media = get_all_media_json()
     return jsonify(all_media)
    
@media_views.route('/api/media', methods=['POST'])
def create_media_action():
    data = request.json
    res = create_media(data['tagEventId'], data['filename'], data['url'])
    if res: 
        return jsonify({'message': f"media {data['filename']} created"}), 201
    return jsonify({'message': f"error creating media"}), 401

#get media by media id
@media_views.route('/api/media/<int:mediaId>', methods=['GET'])
def get_media_by_id_action(mediaId):
     media = get_media(mediaId)
     return jsonify(media.toJSON()), 200

#delete media
@media_views.route('/api/media/delete/<int:mediaId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(mediaId):
  
    media = get_media(mediaId)

    if not media:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_media(mediaId)
    return jsonify(message="media deleted!"), 200