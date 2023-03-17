from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_orgEvent,
    get_orgEvent,
    get_all_orgEvent_json,
)

orgEvent_views = Blueprint('orgEvent_views', __name__, template_folder='../templates')

@orgEvent_views.route('/api/orgEvent', methods=['GET'])
def get_orgEvent_action():
     all_orgEvent = get_all_orgEvent_json()
     return jsonify(all_orgEvent)
    #pass

@orgEvent_views.route('/api/orgEvent', methods=['POST'])
def create_orgEvent_action():
    data = request.json
    res = create_orgEvent(data['userId'], data['organizationId'], data['sex'], data['name'], data['time'], data['location'], data['timestamp'])
    if res: 
        return jsonify({'message': f"orgEvent {data['description']} created"}), 201
    return jsonify({'message': f"error creating orgEvent"}), 401
