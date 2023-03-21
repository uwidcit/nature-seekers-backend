from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent
from datetime import date, datetime, time, timedelta

from App.controllers import (
    create_orgEvent,
    get_orgEvent,
    get_all_orgEvent_json,
    delete_orgEvent
)

orgEvent_views = Blueprint('orgEvent_views', __name__, template_folder='../templates')

@orgEvent_views.route('/api/orgEvent', methods=['GET'])
def get_orgEvent_action():
     all_orgEvent = get_all_orgEvent_json()
     return jsonify(all_orgEvent)
    #pass

@orgEvent_views.route('/api/orgEvent', methods=['POST'])
@jwt_required()
def create_orgEvent_action():
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

    #get data as python date object
    date_components = data["time"].split('-')
    year, month, day = [int(item) for item in date_components]
    timeV=date(year, month, day)

    res = create_orgEvent(userId, data['organizationId'], data['name'], timeV, data['location'])
    if res: 
        return jsonify({'message': f"orgEvent {data['name']} created"}), 201
    return jsonify({'message': f"error creating orgEvent"}), 401


#get orgEvent by orgEvent id
@orgEvent_views.route('/api/orgEvent/<int:orgEventId>', methods=['GET'])
def get_orgEvent_by_id_action(orgEventId):
     orgEvent = get_orgEvent(orgEventId)
     return jsonify(orgEvent.toJSON()), 200

#delete orgEvent
@orgEvent_views.route('/api/orgEvent/delete/<int:orgEventId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(orgEventId):
  
    orgEvent = get_orgEvent(orgEventId)

    if not orgEvent:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_orgEvent(orgEventId)
    return jsonify(message="orgEvent deleted!"), 200