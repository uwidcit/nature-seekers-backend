from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleTag,
    get_turtleTag,
    get_all_turtleTag_json,
    delete_turtleTag, 
    approve
)

turtleTag_views = Blueprint('turtleTag_views', __name__, template_folder='../templates')


@turtleTag_views.route('/api/turtleTag', methods=['GET'])
def get_turtleTag_action():
     all_turtleTag = get_all_turtleTag_json()
     return jsonify(all_turtleTag)

@turtleTag_views.route('/api/turtleTag', methods=['POST'])
@jwt_required()
def create_turtleTag_action():
    data = request.json

    res = create_turtleTag(turtle_id=data['turtle_id'], status= data['status'], location=data['location'])
    if res: 
        return jsonify({'message': f"turtleTag created"}), 201
    return jsonify({'message': f"error creating turtleTag"}), 401

#get turtleTag by turtleTag id
@turtleTag_views.route('/api/turtleTag/<int:turtleTagId>', methods=['GET'])
def get_turtleTag_by_id_action(turtleTagId):
     turtleTag = get_turtleTag(turtleTagId)
     return jsonify(turtleTag .toJSON()), 200

#delete turtleTag
@turtleTag_views.route('/api/turtleTag/delete/<int:turtleTagId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(turtleTagId):
  
    turtleTag = get_turtleTag(turtleTagId)

    if not turtleTag:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleTag(turtleTagId)
    return jsonify(message="turtleTag deleted!"), 200
