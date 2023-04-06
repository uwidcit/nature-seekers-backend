from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Citizen, Organization

from App.controllers import (
    create_turtleBio,
    get_turtleBio,
    get_all_turtleBio_json,
    delete_turtleBio,
    get_turtleBio_by_turtle
)

turtleBio_views = Blueprint('turtleBio_views', __name__, template_folder='../templates')


@turtleBio_views.route('/api/turtleBio', methods=['GET'])
def get_turtleBio_action():
     all_turtleBio = get_all_turtleBio_json()
     return jsonify(all_turtleBio)

@turtleBio_views.route('/api/turtleBio', methods=['POST'])
def create_turtleBio_action():
    data = request.json

    res = create_turtleBio(turtle_id=data['turtle_id'], length=data['length'], width=data['width'], weight=data['weight'])
    if res: 
        return jsonify({'message': f"turtleBio created"}), 201
    return jsonify({'message': f"error creating turtleBio"}), 401

#get turtleBio by turtleBio id
@turtleBio_views.route('/api/turtleBio/<int:turtleBioId>', methods=['GET'])
def get_turtleBio_by_id_action(turtleBioId):
     turtleBio = get_turtleBio(turtleBioId)
     return jsonify(turtleBio .toJSON()), 200

#get turtleBoi by turtle id
@turtleBio_views.route('/api/turtleBio/turtle/<int:turtleid>', methods=['GET'])
def get_turtleBio_by_turtle_action(turtleid):
    turtleBio = get_turtleBio_by_turtle(turtleid)
    return jsonify(turtleBio), 200

#delete turtleBio
@turtleBio_views.route('/api/turtleBio/delete/<int:turtleBioId>', methods=['DELETE'])
def delete_capture_action(turtleBioId):
  
    turtleBio = get_turtleBio(turtleBioId)

    if not turtleBio:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtleBio(turtleBioId)
    return jsonify(message="turtleBio deleted!"), 200
