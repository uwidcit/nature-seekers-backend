from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleEvent,
    get_turtleEvent,
    get_all_turtleEvent_json,
    delete_turtleEvent, 
    update_turtleEvent,
    get_unverified_turtleEvents,
    get_turtleBio_by_turtle,
    get_all_turtleEvent_by_type_json,
    approve
)

turtleEvent_views = Blueprint('turtleEvent_views', __name__, template_folder='../templates')

@turtleEvent_views.route('/api/turtleEvent/<type>/turtle/<int:turtleid>', methods=['GET'])
def get_turtleEvent_by_type_action(type, turtleid):
     turtleEvents = get_all_turtleEvent_by_type_json(type, turtleid)
     return jsonify(turtleEvents)


@turtleEvent_views.route('/api/turtleEvent', methods=['GET'])
def get_turtleEvent_action():
     all_turtleEvent = get_all_turtleEvent_json()
     return jsonify(all_turtleEvent)

@turtleEvent_views.route('/api/turtleEvent', methods=['POST'])
@jwt_required()
def create_turtleEvent_action():
    data = request.json

    username = get_jwt_identity() # convert sent token to user name
    
    #retrieve regular user with given username
    citizen = Citizen.query.filter_by(username=username).first()
    if citizen:
        userId = citizen.id
    
    #retrieve admin user with given username
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        userId = admin.id

    #retrieve organization user with given username
    org = Organization.query.filter_by(username=username).first()
    if org:
        userId = org.id

    if(data["verified"]=="True"):
        veri=True
    else: veri=False

    res = create_turtleEvent(turtle_id=data['turtle_id'],user_id= data['user_id'], beach_name=data['beach_name'], latitude=data['latitude'], longitude=data['longitude'], verified=veri, event_type=data["event_type"], isAlive=data["isAlive"])
    if res: 
        return jsonify({'message': f"turtleEvent created"}), 201
    return jsonify({'message': f"error creating turtleEvent"}), 401

#get turtleEvent by turtleEvent id
@turtleEvent_views.route('/api/turtleEvent/<int:turtleEventId>', methods=['GET'])
def get_turtleEvent_by_id_action(turtleEventId):
     turtleEvent = get_turtleEvent(turtleEventId)
     return jsonify(turtleEvent .toJSON()), 200

#get turtleEvent by turtle id
@turtleEvent_views.route('/api/turtleEvent/turtle/<int:turtleid>', methods=['GET'])
def get_turtleEvent_by_turtle_action(turtleid):
    turtleEvent = get_turtleBio_by_turtle(turtleid)
    return jsonify(turtleEvent), 200



#delete turtleEvent
@turtleEvent_views.route('/api/turtleEvent/delete/<int:turtleEventId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(turtleEventId):
  
    turtleEvent = get_turtleEvent(turtleEventId)

    if not turtleEvent:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleEvent(turtleEventId)
    return jsonify(message="turtleEvent deleted!"), 200

#Approve
@turtleEvent_views.route('/api/turtleEvent/approve/<int:turtleEventId>', methods=['PUT'])
def approve_turtleEvent_by_id(turtleEventId):
    event = get_turtleEvent(turtleEventId)
    if not event:
        return jsonify(error="Event not found"), 401
    approve(turtleEventId)
    if(event.verified == False):
        return jsonify(error="not working"), 401
    return jsonify(message="Event Approved"), 200


@turtleEvent_views.route('/api/turtleEvent/edit/<int:turtleEvent_id>', methods=["PUT"])
#@login_required
def edit_turtleEvent_action(turtleEvent_id):
    data = request.json

    turtleEvent=get_turtleEvent(turtleEvent_id)
    
    if not turtleEvent:
        return jsonify(message="Turtle Event not Found!"), 418

    turtleEvent = update_turtleEvent(
                        turtleEvent_id=turtleEvent_id,
                        turtle_id=data["turtle_id"],
                        user_id=data["user_id"],
                        beach_name=data['beach_name'],
                        latitude=data["latitude"],
                        longitude=data["longitude"],
                        event_type=data["event_type"],
                        isAlive=data["isAlive"]
                       )

    #if turtleEvent:
    return jsonify(turtleEvent.toJSON()), 201
    #return jsonify(message="Nest not Changed!"), 418


@turtleEvent_views.route('/api/turtleEvent/unverified')
def get_unverified_turtleEvents_action():
    turtleEvents=get_unverified_turtleEvents()
    return jsonify( turtleEvents)