from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen

from .user import admin_required

from App.controllers import (
    create_excavation,
    get_excavation,
    get_all_excavation_json,
    delete_excavation,
    get_turtleExcavation_by_nest
)

excavation_views = Blueprint(
    'excavation_views', __name__, template_folder='../templates')

# -----------Create Excavation
@excavation_views.route('/api/excavation', methods=['POST'])
@jwt_required()
def create_excavation_action():
    data = request.json

    username = get_jwt_identity()  # convert sent token to user name

    # retrieve regular user with given username
    citizen = Citizen.query.filter_by(username=username).first()
    if citizen:
        userId = citizen.id

    # retrieve admin user with given username
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        userId = admin.id

    res = create_excavation(data['nest_id'])
    if res:
        return jsonify({'message': f"excavation created"}), 201
    return jsonify({'message': f"error creating excavation"}), 401


# -----------Get All Excavations
@excavation_views.route('/api/excavation', methods=['GET'])
def get_excavation_action():
    all_excavation = get_all_excavation_json()
    return jsonify(all_excavation)


# -----------Get Excavation by Id
@excavation_views.route('/api/excavation/<int:excavationId>', methods=['GET'])
def get_excavation_by_id_action(excavationId):
    excavation = get_excavation(excavationId)
    return jsonify(excavation .toJSON()), 200

# get turtleBoi by nest id
@excavation_views.route('/api/excavation/nest/<int:nest_id>', methods=['GET'])
def get_turtleExcavation_by_nest_action(nest_id):
    turtleExcavation = get_turtleExcavation_by_nest(nest_id)
    return jsonify(turtleExcavation), 200


# -----------Delete Excavation by Id
@excavation_views.route('/api/excavation/delete/<int:excavationId>', methods=['DELETE'])
def delete_capture_action(excavationId):

    excavation = get_excavation(excavationId)

    if not excavation:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_excavation(excavationId)
    return jsonify(message="excavation deleted!"), 200
