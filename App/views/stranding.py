from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_stranding,
    get_stranding,
    get_all_stranding_json,
)

stranding_views = Blueprint('stranding_views', __name__, template_folder='../templates')

@stranding_views.route('/api/stranding', methods=['GET'])
def get_stranding_action():
     all_stranding = get_all_stranding_json()
     return jsonify(all_stranding)
    #pass

@stranding_views.route('/api/stranding', methods=['POST'])
def create_stranding_action():
    data = request.json
    res = create_stranding(data['turtleId'], data['userId'], data['timestamp'], data['comments'])
    if res: 
        return jsonify({'message': f"stranding {data['description']} created"}), 201
    return jsonify({'message': f"error creating stranding"}), 401
