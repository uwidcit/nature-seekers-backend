from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_nestActivity,
    get_nestActivity,
    get_all_nestActivity_json,
    delete_nestActivity,
    update_nestActivity,
    get_turtleActivity_by_nest
)

nestActivity_views = Blueprint('nestActivity_views', __name__, template_folder='../templates')


@nestActivity_views.route('/api/nestActivity', methods=['GET'])
def get_nestActivity_action():
     all_nestActivity = get_all_nestActivity_json()
     return jsonify(all_nestActivity)

@nestActivity_views.route('/api/nestActivity', methods=['POST'])
def create_nestActivity_action():
    data = request.json

    res = create_nestActivity(nest_id=data["nest_id"], name=data["name"], timestamp=data['timestamp'])
    if res: 
        return jsonify(res.toJSON()), 201
    return jsonify({'message': f"error creating nestActivity"}), 401

#----------get nestActivity by nestActivity id
@nestActivity_views.route('/api/nestActivity/<int:nestActivityId>', methods=['GET'])
def get_nestActivity_by_id_action(nestActivityId):
     nestActivity = get_nestActivity(nestActivityId)
     return jsonify(nestActivity .toJSON()), 200

#get turtleActivity by nest id
@nestActivity_views.route('/api/nestActivity/nest/<int:nest_id>', methods=['GET'])
def get_turtleActivity_by_nest_action(nest_id):
    turtleActivity = get_turtleActivity_by_nest(nest_id)
    return jsonify(turtleActivity), 200

#----------delete nestActivity
@nestActivity_views.route('/api/nestActivity/delete/<int:nestActivityId>', methods=['DELETE'])
def delete_capture_action(nestActivityId):
  
    nestActivity = get_nestActivity(nestActivityId)

    if not nestActivity:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nestActivity(nestActivityId)
    return jsonify(message="nestActivity deleted!"), 200

#----------Edit Nest Activity
@nestActivity_views.route('/api/nestActivity/edit/<int:nestActivity_id>', methods=["PUT"])
def edit_nestActivity_action(nestActivity_id):
    data = request.json

    nestActivity=get_nestActivity(nestActivity_id)
    
    if not nestActivity:
        return jsonify(message="Nest not Found!"), 418

    nestActivity = update_nestActivity(nestActivity_id=nestActivity_id, Activity=data["Activity"])

    if nestActivity:
        return jsonify(nestActivity.toJSON()), 201
    return jsonify(message="Nest not Changed!"), 418
