from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleInjury,
    get_turtleInjury,
    get_all_turtleInjury_json,
    delete_turtleInjury, 
    edit_turtleInjury,
    get_turtleInjury_by_turtle
)

turtleInjury_views = Blueprint('turtleInjury_views', __name__, template_folder='../templates')


@turtleInjury_views.route('/api/turtleInjury', methods=['GET'])
def get_turtleInjury_action():
     all_turtleInjury = get_all_turtleInjury_json()
     return jsonify(all_turtleInjury)

@turtleInjury_views.route('/api/turtleInjury', methods=['POST'])
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
     if turtleInjury:
        return jsonify(turtleInjury .toJSON()), 200
     return []

#get turtleInjury by turtle id
@turtleInjury_views.route('/api/turtleInjury/turtle/<int:turtleid>', methods=['GET'])
def get_turtleInjury_by_turtle_action(turtleid):
    turtleInjury = get_turtleInjury_by_turtle(turtleid)
    return jsonify(turtleInjury), 200

#delete turtleInjury
@turtleInjury_views.route('/api/turtleInjury/delete/<int:turtleInjuryId>', methods=['DELETE'])
def delete_capture_action(turtleInjuryId):
  
    turtleInjury = get_turtleInjury(turtleInjuryId)

    if not turtleInjury:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleInjury(turtleInjuryId)
    return jsonify(message="turtleInjury deleted!"), 200

@turtleInjury_views.route('/api/turtleInjury/edit/<int:turtleInjuryid>', methods=['PUT'])
def edit_turtleInjury_action(turtleInjuryid):
    data = request.json

    turtleInjury = get_turtleInjury(turtleInjuryid)

    if not turtleInjury:
        return jsonify(message="Turtle Injury not Found!"), 418
    
    turtleInjury = edit_turtleInjury(turtleInjuryid=turtleInjuryid, description=data["description"])
    if( turtleInjury.description == data["description"]):
        return turtleInjury.toJSON()
    
    return jsonify(message="Turtle Injury not Changed!"), 400
