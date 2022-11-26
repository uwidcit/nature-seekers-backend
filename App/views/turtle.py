from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

# from App.controllers import (
#      get_all_turtles_json
# )

turtle_views = Blueprint('turtle_views', __name__, template_folder='../templates')

@turtle_views.route('/api/turtles', methods=['GET'])
def get_turtle_action():
    turtles = []
    # tutles = get_all_turtles_json()
    return jsonify(turtles)