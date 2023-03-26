from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleActivity,
    get_turtleActivity,
    get_all_turtleActivity_json,
    delete_turtleActivity, 
    edit_turtleActivity,
    approve
)

turtleActivity_views = Blueprint('turtleActivity_views', __name__, template_folder='../templates')


@turtleActivity_views.route('/api/turtleActivity', methods=['GET'])
def get_turtleActivity_action():
     all_turtleActivity = get_all_turtleActivity_json()
     return jsonify(all_turtleActivity)

@turtleActivity_views.route('/api/turtleActivity', methods=['POST'])
@jwt_required()
def create_turtleActivity_action():
    data = request.json

    res = create_turtleActivity(turtle_id=data['turtle_id'], activity=data['activity'])
    if res: 
        return jsonify({'message': f"turtleActivity created"}), 201
    return jsonify({'message': f"error creating turtleActivity"}), 401

#get turtleActivity by turtleActivity id
@turtleActivity_views.route('/api/turtleActivity/<int:turtleActivityId>', methods=['GET'])
def get_turtleActivity_by_id_action(turtleActivityId):
     turtleActivity = get_turtleActivity(turtleActivityId)
     return jsonify(turtleActivity .toJSON()), 200

#delete turtleActivity
@turtleActivity_views.route('/api/turtleActivity/delete/<int:turtleActivityId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(turtleActivityId):
  
    turtleActivity = get_turtleActivity(turtleActivityId)

    if not turtleActivity:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleActivity(turtleActivityId)
    return jsonify(message="turtleActivity deleted!"), 200

@turtleActivity_views.route('/api/turtleActivity/edit/<int:turtleActivityid>', methods=['PUT'])
def edit_turtleActivity_action(turtleActivityid):
    data = request.json

    turtleActivity = get_turtleActivity(turtleActivityid)

    if not turtleActivity:
        return jsonify(message="Turtle Activity not Found!"), 418
    
    turtleActivity = edit_turtleActivity(turtleActivityid=turtleActivityid, activity=data["activity"])
    if( turtleActivity.activity.name == data["activity"]):
        return turtleActivity.toJSON()
    
    return jsonify(message="Turtle Activity not Changed!"), 400
