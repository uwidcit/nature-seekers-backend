from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from .user import admin_required

from App.controllers import (
    create_nest,
    get_nest,
    get_all_nests_json,
    delete_nest,
    update_nest
)

nest_views = Blueprint('nest_views', __name__, template_folder='../templates')


#-----------Create Nest
@nest_views.route('/api/nests', methods=['POST'])
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


#-----------Get Nest by Id
@nest_views.route('/api/nests/<int:nestid>', methods=['GET'])
def get_nest_action(nestid):
    nest = get_nest(nestid)

    if nest:
        return jsonify(nest.toJSON()), 200

    return jsonify({"error": "nest not found"}), 404


#-----------Get All Nests
@nest_views.route('/api/nests', methods=['GET'])
def get_all_nest_action():
    #nests = []
    nests = get_all_nests_json()

    return jsonify(nests)


#-----------Delete Nest by Id
@nest_views.route('/api/nests/delete/<int:nestid>', methods=['DELETE'])
def delete_nest_action(nestid):
  
    nest = get_nest(nestid)

    if not nest:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_nest(nestid)
    return jsonify(message="nest deleted!"), 200


#-----------Edit Nest by Id
@nest_views.route('/api/nests/edit/<int:nest_id>', methods=["PUT"])
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
