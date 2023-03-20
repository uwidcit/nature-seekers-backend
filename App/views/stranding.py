from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_stranding,
    get_stranding,
    get_all_stranding_json,
    delete_stranding
)

stranding_views = Blueprint('stranding_views', __name__, template_folder='../templates')

@stranding_views.route('/api/stranding', methods=['GET'])
def get_stranding_action():
     all_stranding = get_all_stranding_json()
     return jsonify(all_stranding)
    #pass

@stranding_views.route('/api/stranding', methods=['POST'])
@jwt_required()
def create_stranding_action():
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

    res = create_stranding(userId, data['turtleId'], data['comments'])
    if res: 
        return jsonify({'message': f"stranding {data['comments']} created"}), 201
    return jsonify({'message': f"error creating stranding"}), 401

#get stranding by stranding id
@stranding_views.route('/api/stranding/<int:strandingId>', methods=['GET'])
def get_stranding_by_id_action(strandingId):
     stranding = get_stranding(strandingId)
     return jsonify(stranding.toJSON()), 200

#delete stranding
@stranding_views.route('/api/stranding/delete/<int:strandingId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(strandingId):
  
    stranding = get_stranding(strandingId)

    if not stranding:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_stranding(strandingId)
    return jsonify(message="stranding deleted!"), 200