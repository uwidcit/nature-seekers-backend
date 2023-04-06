from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_nestRelocation,
    get_nestRelocation,
    get_all_nestRelocation_json,
    delete_nestRelocation
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
                                from_location_name=data["from_location_name"], 
                                from_latitude=data["from_latitude"], 
                                from_longitude=data["from_longitude"], 
                                from_zone=data["from_zone"], 
                                from_distance_from_vege=data["from_distance_from_vege"], 
                                from_distance_from_high_water=data["from_distance_from_high_water"], 
                                to_location_name=data["to_location_name"],
                                to_latitude=data["to_latitude"], 
                                to_longitude=data["to_longitude"], 
                                to_zone=data["to_zone"], 
                                to_distance_from_vege=data["to_distance_from_vege"], 
                                to_distance_from_high_water=data["to_distance_from_high_water"])
    if res: 
        return jsonify({'message': f"nestRelocation created"}), 201
    return jsonify({'message': f"error creating nestRelocation"}), 401

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

