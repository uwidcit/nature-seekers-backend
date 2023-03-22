from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime

from App.controllers import (
    create_turtle,
    get_turtle,
    get_all_turtles_json,
    delete_turtle
)

turtle_views = Blueprint('turtle_views', __name__, template_folder='../templates')

@turtle_views.route('/api/turtles', methods=['POST'])
#@jwt_required()
def create_turtle_action():
    data = request.json

    #get data as python date object
    date_components = data["dob"].split('-')
    year, month, day = [int(item) for item in date_components]
    dob = date(year, month, day)

    turtle = create_turtle(name=data["name"], sex=data["sex"], dob=dob, species=data["species"])

    if turtle:
        return jsonify(turtle.toJSON()), 201

    return jsonify({"error": "turtle not created"}), 400


@turtle_views.route('/api/turtles/<int:turtleid>', methods=['GET'])
#@jwt_required()
def get_turtle_action(turtleid):
    turtle = get_turtle(turtleid)

    if turtle:
        return jsonify(turtle.toJSON()), 200

    return jsonify({"error": "turtle not found"}), 404


@turtle_views.route('/api/turtles', methods=['GET'])
#@jwt_required()
def get_all_turtle_action():
    #turtles = []
    turtles = get_all_turtles_json()

    return jsonify(turtles)


@turtle_views.route('/api/turtles/delete/<int:turtleid>', methods=['DELETE'])
#@jwt_required()
def delete_turtle_action(turtleid):
  
    turtle = get_turtle(turtleid)

    if not turtle:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtle(turtleid)
    return jsonify(message="turtle deleted!"), 200

