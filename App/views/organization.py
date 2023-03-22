from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import User, Admin, Contributor, TagEvent

from App.controllers import (
    create_organization,
    get_organization,
    get_all_organization_json,
    delete_organization,
    edit_organization_data
) 

organization_views = Blueprint('organization_views', __name__, template_folder='../templates')

@organization_views.route('/api/organization', methods=['GET'])
def get_organization_action():
     all_organization = get_all_organization_json()
     return jsonify(all_organization)
    
@organization_views.route('/api/organization', methods=['POST'])
@jwt_required()
def create_organization_action():
    data = request.json

    res = create_organization(data['description'], data['email'], data['phone'], data['website'])
    if res: 
        return jsonify({'message': f"organization {data['description']} created"}), 201
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


#Edit organization by organization id
@organization_views.route('/api/organization/edit/<int:organizationId>', methods=['PUT'])
def edit_organization_by_id_action(organizationId):
    data = request.json

    org = get_organization(organizationId)

    if org:
        edit_organization_data(organizationId, data["description"], data["email"], data["phone"], data["website"])

    return (org.toJSON()), 200

