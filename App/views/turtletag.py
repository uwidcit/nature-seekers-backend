from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_turtle_tag,
    get_turtle_tag,
    get_all_turtletags_json,
    delete_turtle_tag
)

turtle_tag_views = Blueprint('turtle_tag_views', __name__, template_folder='../templates')

@turtle_tag_views.route('/api/turtletag', methods=['POST'])
#@jwt_required()
def create_turtle_tag_action():
    data = request.json
    turtle_tag = create_turtle_tag(tageventid=data["tageventid"], code=data["code"], status=data["status"], location=data["location"])

    if turtle_tag:
        return jsonify(turtle_tag.toJSON()), 201

    return jsonify({"error": "turtle tag not created"}), 400


@turtle_tag_views.route('/api/turtletag/<int:turtletagid>', methods=['GET'])
#@jwt_required()
def get_turtle_tag_action(turtletagid):
    turtle_tag = get_turtle_tag(turtletagid)

    if turtle_tag:
        return jsonify(turtle_tag.toJSON()), 200
        
    return jsonify({"error": "turtle tag not found"}), 404


@turtle_tag_views.route('/api/turtletag', methods=['GET'])
#@jwt_required()
def get_all_turtle_tag_action():
    turtle_tags = get_all_turtletags_json()

    return jsonify(turtle_tags)


#delete turtletag
@turtle_tag_views.route('/api/turtletag/delete/<int:turtletagId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(turtletagId):
  
    turtletag = get_turtle_tag(turtletagId)

    if not turtletag:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_turtle_tag(turtletagId)
    return jsonify(message="turtletag deleted!"), 200   

