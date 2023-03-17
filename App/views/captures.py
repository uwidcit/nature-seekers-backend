from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_capture,
    get_capture,
    get_all_capture_json,
)

captures_views = Blueprint('captures_views', __name__, template_folder='../templates')

@captures_views.route('/api/capture', methods=['GET'])
def get_capture_action():
     all_capture = get_all_capture_json()
     return jsonify(all_capture)
    #pass

@captures_views.route('/api/capture', methods=['POST'])
def create_capture_action():
    data = request.json
    res = create_capture(data['turtleId'], data['userId'], data['timestamp'], data['comments'])
    if res: 
        return jsonify({'message': f"capture {data['description']} created"}), 201
    return jsonify({'message': f"error creating capture"}), 401

