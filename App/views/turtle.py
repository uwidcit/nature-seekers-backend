from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_turtle,
    get_turtle,
    get_all_turtles_json,
)

turtle_views = Blueprint('turtle_views', __name__, template_folder='../templates')

@turtle_views.route('/api/turtles', methods=['POST'])
#@jwt_required()
def create_turtle_action():
    data = request.json
    turtle = create_turtle(name=data["name"], sex=data["sex"], dob=data["dob"])

    if turtle:
        return jsonify(turtle.toJSON()), 201

    return jsonify({"error": "turtle not created"}), 400


@turtle_views.route('/api/turtles/<int:turtleid>', methods=['GET'])
#@jwt_required()
def get_turtle_action(turtleid):
    turtle = get_turtle(turtleid)

    if turtle:
        return jsonify(turtle.toJSON), 200

    return jsonify({"error": "turtle not found"}), 404


@turtle_views.route('/api/turtles', methods=['GET'])
#@jwt_required()
def get_all_turtle_action():
    #turtles = []
    turtles = get_all_turtles_json()

    return jsonify(turtles)

