from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleInjury,
    get_turtleInjury,
    get_all_turtleInjury_json,
    delete_turtleInjury, 
    approve
)

turtleInjury_views = Blueprint('turtleInjury_views', __name__, template_folder='../templates')


@turtleInjury_views.route('/api/turtleInjury', methods=['GET'])
def get_turtleInjury_action():
     all_turtleInjury = get_all_turtleInjury_json()
     return jsonify(all_turtleInjury)

@turtleInjury_views.route('/api/turtleInjury', methods=['POST'])
@jwt_required()
def create_turtleInjury_action():
    data = request.json

    res = create_turtleInjury(turtle_id=data['turtle_id'], description= data['description'])
    if res: 
        return jsonify({'message': f"turtleInjury created"}), 201
    return jsonify({'message': f"error creating turtleInjury"}), 401

#get turtleInjury by turtleInjury id
@turtleInjury_views.route('/api/turtleInjury/<int:turtleInjuryId>', methods=['GET'])
def get_turtleInjury_by_id_action(turtleInjuryId):
     turtleInjury = get_turtleInjury(turtleInjuryId)
     return jsonify(turtleInjury .toJSON()), 200

#delete turtleInjury
@turtleInjury_views.route('/api/turtleInjury/delete/<int:turtleInjuryId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(turtleInjuryId):
  
    turtleInjury = get_turtleInjury(turtleInjuryId)

    if not turtleInjury:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleInjury(turtleInjuryId)
    return jsonify(message="turtleInjury deleted!"), 200

#Approve
@turtleInjury_views.route('/api/turtleInjury/approve/<int:turtleInjuryId>', methods=['PUT'])
def approve_turtleInjury_by_id(turtleInjuryId):
    event = get_turtleInjury(turtleInjuryId)
    if not event:
        return jsonify(error="Event not found"), 401
    approve(turtleInjuryId)
    if(event.verified == False):
        return jsonify(error="not working"), 401
    return jsonify(message="Event Approved"), 200