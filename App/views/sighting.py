from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_sighting,
    get_sighting,
    get_all_sighting_json,
    delete_sighting
)

sighting_views = Blueprint('sighting_views', __name__, template_folder='../templates')

@sighting_views.route('/api/sighting', methods=['GET'])
def get_sighting_action():
     all_sighting = get_all_sighting_json()
     return jsonify(all_sighting)
    #pass

@sighting_views.route('/api/sighting', methods=['POST'])
@jwt_required()
def create_sighting_action():
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

    res = create_sighting(userId, data['turtleId'], data['lat'], data['long'], data['comments'])
    if res: 
        return jsonify({'message': f"sighting {data['comments']} created"}), 201
    return jsonify({'message': f"error creating sighting"}), 401

#get sighting by sighting id
@sighting_views.route('/api/sighting/<int:sightingId>', methods=['GET'])
def get_sighting_by_id_action(sightingId):
     sighting = get_sighting(sightingId)
     return jsonify(sighting.toJSON()), 200

#delete sighting
@sighting_views.route('/api/sighting/delete/<int:sightingId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(sightingId):
  
    sighting = get_sighting(sightingId)

    if not sighting:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_sighting(sightingId)
    return jsonify(message="sighting deleted!"), 200