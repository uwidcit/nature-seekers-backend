from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_tag_event,
    get_tag_event,
    get_all_tag_events_json,
)

tag_event_views = Blueprint('tag_event_views', __name__, template_folder='../templates')

@tag_event_views.route('/api/tagevent', methods=['POST'])
#@jwt_required()
def create_turtle_action():
    data = request.json
    tag_event = create_tag_event(turtleid=data["turtleid"], userid=data["userid"], comments=data["comments"], weight=data["weight"], length=data["length"], lat=data["lat"], lon=data["lon"], approved=data["approved"])

    if tag_event:
        return jsonify(tag_event.toJSON()), 201

    return jsonify({"error": "tag event not created"}), 400


@tag_event_views.route('/api/tagevent/<int:tageventid>', methods=['GET'])
#@jwt_required()
def get_tag_event_action(tageventid):
    tag_event = get_tag_event(tageventid)

    if tag_event:
        return jsonify(tag_event.toJSON()), 200

    return jsonify({"error": "tag event not found"}), 404


@tag_event_views.route('/api/tagevent', methods=['GET'])
#@jwt_required()
def get_all_tag_events_action():
    tag_events = get_all_tag_events_json()

    return jsonify(tag_events)

