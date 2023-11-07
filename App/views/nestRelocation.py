from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_nestRelocation,
    get_nestRelocation,
    get_all_nestRelocation_json,
    delete_nestRelocation,
    get_turtleRelocation_by_nest_id
)

nestRelocation_views = Blueprint('nestRelocation_views', __name__, template_folder='../templates')


@nestRelocation_views.route('/api/nestRelocation', methods=['GET'])
def get_nestRelocation_action():
     all_nestRelocation = get_all_nestRelocation_json()
     return jsonify(all_nestRelocation)

@nestRelocation_views.route('/api/nestRelocation', methods=['POST'])
def create_nestRelocation_action():
    data = request.json

    res = create_nestRelocation(nest_id=data["nest_id"], 
                                to_location_name=data["location_name"],
                                to_latitude=data["latitude"], 
                                to_longitude=data["longitude"], 
                                to_zone=data["zone"], 
                                to_timestamp=data['timestamp'],
                                )
    if res: 
        return jsonify(res.toJSON()), 201
    return jsonify({'message': f"error creating nestRelocation"}), 401

#get turtleRelocation by nest id
@nestRelocation_views.route('/api/nestRelocation/nest/<int:nest_id>', methods=['GET'])
def get_turtleRelocation_by_nest_action(nest_id):
    turtleRelocation = get_turtleRelocation_by_nest_id(nest_id)
    return jsonify(turtleRelocation), 200


#get nestRelocation by nestRelocation id
@nestRelocation_views.route('/api/nestRelocation/<int:nestRelocationId>', methods=['GET'])
def get_nestRelocation_by_id_action(nestRelocationId):
     nestRelocation = get_nestRelocation(nestRelocationId)
     return jsonify(nestRelocation .toJSON()), 200

#delete nestRelocation
@nestRelocation_views.route('/api/nestRelocation/delete/<int:nestRelocationId>', methods=['DELETE'])
def delete_capture_action(nestRelocationId):
  
    nestRelocation = get_nestRelocation(nestRelocationId)

    if not nestRelocation:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nestRelocation(nestRelocationId)
    return jsonify(message="nestRelocation deleted!"), 200

