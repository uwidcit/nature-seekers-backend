from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleEventMedia,
    get_turtleEventMedia,
    get_all_turtleEventMedia_json,
    delete_turtleEventMedia, 
    approve
)

turtleEventMedia_views = Blueprint('turtleEventMedia_views', __name__, template_folder='../templates')


@turtleEventMedia_views.route('/api/turtleEventMedia', methods=['GET'])
def get_turtleEventMedia_action():
     all_turtleEventMedia = get_all_turtleEventMedia_json()
     return jsonify(all_turtleEventMedia)

@turtleEventMedia_views.route('/api/turtleEventMedia', methods=['POST'])
def create_turtleEventMedia_action():
    data = request.json

    res = create_turtleEventMedia(event_id=data['event_id'],url= data['url'], filename=data['filename'])
    if res: 
        return jsonify({'message': f"turtleEventMedia created"}), 201
    return jsonify({'message': f"error creating turtleEventMedia"}), 401

#----------get turtleEventMedia by turtleEventMedia id
@turtleEventMedia_views.route('/api/turtleEventMedia/<int:turtleEventMediaId>', methods=['GET'])
def get_turtleEventMedia_by_id_action(turtleEventMediaId):
     turtleEventMedia = get_turtleEventMedia(turtleEventMediaId)
     return jsonify(turtleEventMedia .toJSON()), 200

#----------delete turtleEventMedia
@turtleEventMedia_views.route('/api/turtleEventMedia/delete/<int:turtleEventMediaId>', methods=['DELETE'])
def delete_capture_action(turtleEventMediaId):
  
    turtleEventMedia = get_turtleEventMedia(turtleEventMediaId)

    if not turtleEventMedia:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleEventMedia(turtleEventMediaId)
    return jsonify(message="turtleEventMedia deleted!"), 200

#----------Approve
@turtleEventMedia_views.route('/api/turtleEventMedia/approve/<int:turtleEventMediaId>', methods=['PUT'])
def approve_turtleEventMedia_by_id(turtleEventMediaId):
    event = get_turtleEventMedia(turtleEventMediaId)
    if not event:
        return jsonify(error="Event not found"), 401
    approve(turtleEventMediaId)
    if(event.verified == False):
        return jsonify(error="not working"), 401
    return jsonify(message="Event Approved"), 200