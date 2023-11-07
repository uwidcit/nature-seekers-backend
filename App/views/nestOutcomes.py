from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_nestOutcome,
    get_nestOutcome,
    get_all_nestOutcome_json,
    delete_nestOutcome,
    update_nestOutcome,
    get_turtleOutcome_by_nest
)

nestOutcome_views = Blueprint('nestOutcome_views', __name__, template_folder='../templates')


@nestOutcome_views.route('/api/nestOutcome', methods=['GET'])
def get_nestOutcome_action():
     all_nestOutcome = get_all_nestOutcome_json()
     return jsonify(all_nestOutcome)

@nestOutcome_views.route('/api/nestOutcome', methods=['POST'])
def create_nestOutcome_action():
    data = request.json

    res = create_nestOutcome(nest_id=data["nest_id"], outcome=data["outcome"])
    if res: 
        return jsonify(res.toJSON()), 201
    return jsonify({'message': f"error creating nestOutcome"}), 401

#----------get nestOutcome by nestOutcome id
@nestOutcome_views.route('/api/nestOutcome/<int:nestOutcomeId>', methods=['GET'])
def get_nestOutcome_by_id_action(nestOutcomeId):
     nestOutcome = get_nestOutcome(nestOutcomeId)
     return jsonify(nestOutcome .toJSON()), 200

#get turtleOutcome by nest id
@nestOutcome_views.route('/api/nestOutcome/nest/<int:nest_id>', methods=['GET'])
def get_turtleOutcome_by_nest_action(nest_id):
    turtleOutcome = get_turtleOutcome_by_nest(nest_id)
    return jsonify(turtleOutcome), 200

#----------delete nestOutcome
@nestOutcome_views.route('/api/nestOutcome/delete/<int:nestOutcomeId>', methods=['DELETE'])
def delete_capture_action(nestOutcomeId):
  
    nestOutcome = get_nestOutcome(nestOutcomeId)

    if not nestOutcome:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nestOutcome(nestOutcomeId)
    return jsonify(message="nestOutcome deleted!"), 200

#----------Edit Nest Outcome
@nestOutcome_views.route('/api/nestOutcome/edit/<int:nestOutcome_id>', methods=["PUT"])
def edit_nestOutcome_action(nestOutcome_id):
    data = request.json

    nestOutcome=get_nestOutcome(nestOutcome_id)
    
    if not nestOutcome:
        return jsonify(message="Nest not Found!"), 418

    nestOutcome = update_nestOutcome(nestOutcome_id=nestOutcome_id, outcome=data["outcome"])

    if nestOutcome:
        return jsonify(nestOutcome.toJSON()), 201
    return jsonify(message="Nest not Changed!"), 418
