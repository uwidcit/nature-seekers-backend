from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_excavation,
    get_excavation,
    get_all_excavation_json,
    delete_excavation
)

excavation_views = Blueprint('excavation_views', __name__, template_folder='../templates')

@excavation_views.route('/api/excavation', methods=['GET'])
def get_excavation_action():
     all_excavation = get_all_excavation_json()
     return jsonify(all_excavation)

@excavation_views.route('/api/excavation', methods=['POST'])
def create_excavation_action():
    data = request.json

    username = get_jwt_identity() # convert sent token to user name
    
    #retrieve regular user with given username
    contributor = Contributor.query.filter_by(username=username).first()
    if contributor:
        userId = contributor.id
    
    #retrieve admin user with given username
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        userId = admin.id


    res = create_excavation(userId, data['description'], data['lat'], data['lon'])
    if res: 
        return jsonify({'message': f"excavation {data['description']} created"}), 201
    return jsonify({'message': f"error creating excavation"}), 401

#get excavation by excavation id
@excavation_views.route('/api/excavation/<int:excavationId>', methods=['GET'])
def get_excavation_by_id_action(excavationId):
     excavation = get_excavation(excavationId)
     return jsonify(excavation .toJSON()), 200

#delete excavation
@excavation_views.route('/api/excavation/delete/<int:excavationId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(excavationId):
  
    excavation = get_excavation(excavationId)

    if not excavation:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_excavation(excavationId)
    return jsonify(message="excavation deleted!"), 200