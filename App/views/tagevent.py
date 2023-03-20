from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_tag_event,
    get_tag_event,
    get_all_tag_events_json,
    delete_tag_event
)

tag_event_views = Blueprint('tag_event_views', __name__, template_folder='../templates')

@tag_event_views.route('/api/tagevent', methods=['POST'])
@jwt_required()
def create_tag_event_action():
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


    tag_event = create_tag_event(turtleid=data["turtleid"], userid=userId, comments=data["comments"], weight=data["weight"], length=data["length"], lat=data["lat"], lon=data["lon"], approved=data["approved"])

    if tag_event:
        return jsonify(tag_event.toJSON()), 201

    return jsonify({"error": "tag event not created"}), 400


@tag_event_views.route('/api/tagevent/<int:tageventid>', methods=['GET'])
@jwt_required()
def get_tag_event_action(tageventid):
    tag_event = get_tag_event(tageventid)

    if tag_event:
        return jsonify(tag_event.toJSON()), 200

    return jsonify({"error": "tag event not found"}), 404


@tag_event_views.route('/api/tagevent', methods=['GET'])
@jwt_required()
def get_all_tag_events_action():
    tag_events = get_all_tag_events_json()

    return jsonify(tag_events)


#delete tag_event
@tag_event_views.route('/api/tag_event/delete/<int:tag_eventId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(tag_eventId):
  
    tag_event = get_tag_event(tag_eventId)

    if not tag_event:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_tag_event(tag_eventId)
    return jsonify(message="tag_event deleted!"), 200