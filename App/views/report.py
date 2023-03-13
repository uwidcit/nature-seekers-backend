from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from App.controllers import (
    create_report,
    get_report,
    get_all_report_json,
)

report_views = Blueprint('report_views', __name__, template_folder='../templates')

@report_views.route('/api/report', methods=['GET'])
def get_report_action():
     all_report = get_all_report_json()
     return jsonify(all_report)
    #pass

@report_views.route('/api/report', methods=['POST'])
def create_report_action():
    data = request.json
    res = create_report(data['turtleId'], data['userId'], data['timestamp'], data['comments'])
    if res: 
        return jsonify({'message': f"report {data['description']} created"}), 201
    return jsonify({'message': f"error creating report"}), 401
