from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime

from App.controllers import (
    create_nest,
    get_nest,
    get_all_nests_json,
    delete_nest,
    update_nest
)

nest_views = Blueprint('nest_views', __name__, template_folder='../templates')

@nest_views.route('/api/nests', methods=['POST'])
#@jwt_required()
def create_nest_action():
    data = request.json

    nest = create_nest(
                        num_yolked=data["num_yolked"],
                        num_unyolked=data["num_unyolked"], 
                        location_name=data["location_name"],
                        latitude=data["latitude"],
                        longitude=data["longitude"],
                        zone=data["zone"],
                        distance_from_vege=data["distance_from_vege"],
                        distance_from_high_water=data["distance_from_high_water"]
                      )

    if nest:
        return jsonify(nest.toJSON()), 201

    return jsonify({"error": "nest not created"}), 400


@nest_views.route('/api/nests/<int:nestid>', methods=['GET'])
#@jwt_required()
def get_nest_action(nestid):
    nest = get_nest(nestid)

    if nest:
        return jsonify(nest.toJSON()), 200

    return jsonify({"error": "nest not found"}), 404


@nest_views.route('/api/nests', methods=['GET'])
#@jwt_required()
def get_all_nest_action():
    #nests = []
    nests = get_all_nests_json()

    return jsonify(nests)


@nest_views.route('/api/nests/delete/<int:nestid>', methods=['DELETE'])
@jwt_required()
def delete_nest_action(nestid):
  
    nest = get_nest(nestid)

    if not nest:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nest(nestid)
    return jsonify(message="nest deleted!"), 200


@nest_views.route('/api/nests/edit/<int:nest_id>', methods=["PUT"])
#@login_required
def edit_nest_action(nest_id):
    data = request.json

    nest=get_nest(nest_id)
    
    if not nest:
        return jsonify(message="Nest not Found!"), 418

    nest = update_nest(
                        nest_id=nest_id,
                        num_yolked=data["num_yolked"],
                        num_unyolked=data["num_unyolked"],
                        location_name=data['location_name'],
                        latitude=data["latitude"],
                        longitude=data["longitude"],
                        zone=data["zone"],
                        distance_from_vegetation=data["distance_from_vege"],
                        distance_from_high_water= data["distance_from_high_water"]
                       )

    #if nest:
    return jsonify(nest.toJSON()), 201
    #return jsonify(message="Nest not Changed!"), 418
