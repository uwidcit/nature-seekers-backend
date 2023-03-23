from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_nestOutcome,
    get_nestOutcome,
    get_all_nestOutcome_json,
    delete_nestOutcome
)

nestOutcome_views = Blueprint('nestOutcome_views', __name__, template_folder='../templates')


@nestOutcome_views.route('/api/nestOutcome', methods=['GET'])
def get_nestOutcome_action():
     all_nestOutcome = get_all_nestOutcome_json()
     return jsonify(all_nestOutcome)

@nestOutcome_views.route('/api/nestOutcome', methods=['POST'])
@jwt_required()
def create_nestOutcome_action():
    data = request.json

    res = create_nestOutcome(nest_id=data["nest_id"], outcome=data["outcome"])
    if res: 
        return jsonify({'message': f"nestOutcome created"}), 201
    return jsonify({'message': f"error creating nestOutcome"}), 401

#get nestOutcome by nestOutcome id
@nestOutcome_views.route('/api/nestOutcome/<int:nestOutcomeId>', methods=['GET'])
def get_nestOutcome_by_id_action(nestOutcomeId):
     nestOutcome = get_nestOutcome(nestOutcomeId)
     return jsonify(nestOutcome .toJSON()), 200

#delete nestOutcome
@nestOutcome_views.route('/api/nestOutcome/delete/<int:nestOutcomeId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(nestOutcomeId):
  
    nestOutcome = get_nestOutcome(nestOutcomeId)

    if not nestOutcome:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nestOutcome(nestOutcomeId)
    return jsonify(message="nestOutcome deleted!"), 200

