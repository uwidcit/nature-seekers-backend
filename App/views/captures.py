from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_capture,
    get_capture,
    get_all_capture_json,
    delete_capture
)

captures_views = Blueprint('captures_views', __name__, template_folder='../templates')

#get all Captures
@captures_views.route('/api/capture', methods=['GET'])
def get_capture_action():
     all_capture = get_all_capture_json()
     return jsonify(all_capture)
    #pass

#create capture
@captures_views.route('/api/capture', methods=['POST'])
@jwt_required()
def create_capture_action():
    data = request.json

    username = get_jwt_identity() # convert sent token to user name
    
    #retrieve regular user with given username
    contributor = Contributor.query.filter_by(username=username).first()
    if contributor:
        userId = contributor.id
    
    #retrieve admin user with given username
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        userId = admin.id

    res = create_capture(userId, data['turtleId'], data['comments'], )
    if res: 
        return jsonify({'message': f"capture {data['comments']} created"}), 201
    return jsonify({'message': f"error creating capture"}), 401

#get capture by capture id
@captures_views.route('/api/capture/<int:captureId>', methods=['GET'])
def get_capture_by_id_action(captureId):
     capture = get_capture(captureId)
     return jsonify(capture.toJSON()), 200

@captures_views.route('/api/capture/delete/<int:captureId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(captureId):
  
    capture = get_capture(captureId)

    if not capture:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_capture(captureId)
    return jsonify(message="capture deleted!"), 200
