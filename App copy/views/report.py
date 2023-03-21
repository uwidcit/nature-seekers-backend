from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

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

    username = get_jwt_identity() # convert sent token to user name
    
    #retrieve regular user with given username
    contributor = Contributor.query.filter_by(username=username).first()
    if contributor:
        userId = contributor.id
    
    #retrieve admin user with given username
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        userId = admin.id

    res = create_report(userId, data['report'])
    if res: 
        return jsonify({'message': f"report {data['description']} created"}), 201
    return jsonify({'message': f"error creating report"}), 401
