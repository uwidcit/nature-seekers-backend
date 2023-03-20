from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_organization,
    get_organization,
    get_all_organization_json,
    delete_organization
) 

organization_views = Blueprint('organization_views', __name__, template_folder='../templates')

@organization_views.route('/api/organization', methods=['GET'])
def get_organization_action():
     all_organization = get_all_organization_json()
     return jsonify(all_organization)
    
@organization_views.route('/api/organization', methods=['POST'])
def create_organization_action():
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

    res = create_organization(userId, data['description'], data['email'], data['phone'], data['website'])
    if res: 
        return jsonify({'message': f"organization {data['filename']} created"}), 201
    return jsonify({'message': f"error creating organization"}), 401

#get organization by organization id
@organization_views.route('/api/organization/<int:organizationId>', methods=['GET'])
def get_organization_by_id_action(organizationId):
     organization = get_organization(organizationId)
     return jsonify(organization.toJSON()), 200

#delete organization
@organization_views.route('/api/organization/delete/<int:organizationId>', methods=['DELETE'])
@jwt_required()
def delete_capture_action(organizationId):
  
    organization = get_organization(organizationId)

    if not organization:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 401

    delete_organization(organizationId)
    return jsonify(message="organization deleted!"), 200