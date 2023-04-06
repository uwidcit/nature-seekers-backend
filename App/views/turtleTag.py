from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleTag,
    get_turtleTag,
    get_all_turtleTag_json,
    delete_turtleTag, 
    edit_turtleTag,
    get_turtleTag_by_turtle
)

turtleTag_views = Blueprint('turtleTag_views', __name__, template_folder='../templates')


@turtleTag_views.route('/api/turtleTag', methods=['GET'])
def get_turtleTag_action():
     all_turtleTag = get_all_turtleTag_json()
     return jsonify(all_turtleTag)

@turtleTag_views.route('/api/turtleTag', methods=['POST'])
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

#get turtleTag by turtle id
@turtleTag_views.route('/api/turtleTag/turtle/<int:turtleid>', methods=['GET'])
def get_turtleTag_by_turtle_action(turtleid):
    turtleTag = get_turtleTag_by_turtle(turtleid)
    return jsonify(turtleTag), 200


#delete turtleTag
@turtleTag_views.route('/api/turtleTag/delete/<int:turtleTagId>', methods=['DELETE'])
def delete_capture_action(turtleTagId):
  
    turtleTag = get_turtleTag(turtleTagId)

    if not turtleTag:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleTag(turtleTagId)
    return jsonify(message="turtleTag deleted!"), 200


@turtleTag_views.route('/api/turtleTag/edit/<int:turtleTagid>', methods=['PUT'])
def edit_turtleTag_action(turtleTagid):
    data = request.json

    turtleTag = get_turtleTag(turtleTagid)

    if not turtleTag:
        return jsonify(message="Turtle Tag not Found!"), 418
    
    turtleTag = edit_turtleTag(turtleTagid=turtleTagid, status=data["status"])
    if( turtleTag.status.name == data["status"]):
        return turtleTag.toJSON()
    
    return jsonify(message="Turtle Tag not Changed!"), 400
