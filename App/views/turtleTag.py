from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleTag,
    get_turtleTag,
    get_all_turtleTag_json,
    delete_turtleTag, 
    edit_turtleTag,
    get_turtleTag_by_turtle,
    get_turtle_tag_by_turtle_and_tag
)

turtleTag_views = Blueprint('turtleTag_views', __name__, template_folder='../templates')


@turtleTag_views.route('/api/turtleTags', methods=['GET'])
def get_all_turtleTag_action():
    data = request.args
    all_turtleTag = get_all_turtleTag_json()
    return jsonify(all_turtleTag)

@turtleTag_views.route('/api/turtleTag', methods=['GET'])
def get_turtleTag_action():
    data = request.args

    all_turtleTag = get_turtle_tag_by_id(data.get('tag_id'),)
    return jsonify(all_turtleTag.toJSON())

@turtleTag_views.route('/api/turtleTag', methods=['POST'])
def create_turtleTag_action():
    data = request.json
    res = create_turtleTag(tag_id = int(data['tag_id']), turtle_id=int(data['turtle_id']), location=data['location'])
    if res: 
        return jsonify(res.toJSON()), 201
    return jsonify({'message': f"error creating turtleTag"}), 401

#get turtleTag by turtleTag id
@turtleTag_views.route('/api/turtleTag/<int:turtleTagId>', methods=['GET'])
def get_turtleTag_by_id_action(turtleTagId):
     turtleTag = get_turtleTag(turtleTagId)
     return jsonify(turtleTag .toJSON() if turtleTag else {}), 200

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

    turtleTag = edit_turtleTag(turtle_tag_id = turtleTagid, turtle_id= int(data['turtle_id']), location= data['location'], status=data["status"])
    if turtleTag:
        return turtleTag.toJSON()
    
    return jsonify(message="Turtle Tag not Changed!"), 400
