from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from App.models import Organization
from datetime import date, datetime

from App.controllers import (
    create_organizationEvent,
    get_organizationEvent,
    get_all_organizationEvent_json,
    delete_organizationEvent
)

organizationEvent_views = Blueprint('organizationEvent_views', __name__, template_folder='../templates')

@organizationEvent_views.route('/api/organizationEvents', methods=['POST'])
@jwt_required()
def create_organizationEvent_action():
    data = request.json

    username = get_jwt_identity() # convert sent token to user name

    #retrieve organization user with given username
    org = Organization.query.filter_by(username=username).first()
    if not org:
        return jsonify({"error": "organization not found"}), 400
    if org:
        userId = org.id
        organizationEvent = create_organizationEvent(
                            organization_id=userId,
                            event_name=data["event_name"]
                        )

    if organizationEvent:
        return jsonify(organizationEvent.toJSON()), 201

    return jsonify({"error": "organizationEvent not created"}), 400


@organizationEvent_views.route('/api/organizationEvents/<int:organizationEventid>', methods=['GET'])
#@jwt_required()
def get_organizationEvent_action(organizationEventid):
    organizationEvent = get_organizationEvent(organizationEventid)

    if organizationEvent:
        return jsonify(organizationEvent.toJSON()), 200

    return jsonify({"error": "organizationEvent not found"}), 404


@organizationEvent_views.route('/api/organizationEvents', methods=['GET'])
#@jwt_required()
def get_all_organizationEvent_action():
    #organizationEvents = []
    organizationEvents = get_all_organizationEvent_json()

    return jsonify(organizationEvents)


@organizationEvent_views.route('/api/organizationEvents/delete/<int:organizationEventid>', methods=['DELETE'])
@jwt_required()
def delete_organizationEvent_action(organizationEventid):
  
    organizationEvent = get_organizationEvent(organizationEventid)

    if not organizationEvent:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_organizationEvent(organizationEventid)
    return jsonify(message="organizationEvent deleted!"), 200

