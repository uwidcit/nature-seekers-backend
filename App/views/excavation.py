from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_excavation,
    get_excavation,
    get_all_excavation_json,
)

excavation_views = Blueprint('excavation_views', __name__, template_folder='../templates')

@excavation_views.route('/api/excavation', methods=['GET'])
def get_excavation_action():
     all_excavation = get_all_excavation_json()
     return jsonify(all_excavation)
    #pass

@excavation_views.route('/api/excavation', methods=['POST'])
def create_excavation_action():
    data = request.json
    res = create_excavation(data['userid'], data['description'], data['lat'], data['lon'])
    if res: 
        return jsonify({'message': f"excavation {data['description']} created"}), 201
    return jsonify({'message': f"error creating excavation"}), 401
