from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_sighting,
    get_sighting,
    get_all_sighting_json,
)

sighting_views = Blueprint('sighting_views', __name__, template_folder='../templates')

@sighting_views.route('/api/sighting', methods=['GET'])
def get_sighting_action():
     all_sighting = get_all_sighting_json()
     return jsonify(all_sighting)
    #pass

@sighting_views.route('/api/sighting', methods=['POST'])
def create_sighting_action():
    data = request.json
    res = create_sighting(data['turtleId'], data['userId'], data['timestamp'], data['comments'])
    if res: 
        return jsonify({'message': f"sighting {data['description']} created"}), 201
    return jsonify({'message': f"error creating sighting"}), 401
