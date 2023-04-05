from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import current_user, login_required, login_user, logout_user

##stuff for identify
from App.models import User, Admin, Citizen, TurtleEvent


from App.controllers import (
    create_citizen,
    create_admin, 
    create_organization,
    get_all_users,
    get_all_users_json,
    login,
    get_all_organizations_json,
    delete_organization,
    #citizen_login
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

##  Create users 

@user_views.route('/api/citizens', methods=['POST'])
def create_citizen_action():
    data = request.json
    res = create_citizen(data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res: 
        return jsonify({'message': f"citizen user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401

@user_views.route('/api/admins', methods=['POST'])
def create_admin_action():
    data = request.json
    res = create_admin(data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res: 
        return jsonify({'message': f"admin user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401

@user_views.route('/api/organization', methods=['POST'])
def create_organization_action():
    data = request.json
    res = create_organization(data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res: 
        return jsonify({'message': f"organization user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401

@user_views.route('/api/organization', methods=['GET'])
def get_all_organizations_action():
  organizations = get_all_organizations_json()
  return jsonify(organizations)


@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


#Login Users
@user_views.route('/login', methods=['POST'])
def login_view():
  data = request.json

  user = User.query.filter_by(username=data['username']).first()

  if user and user.check_password(data['password']):
    login_user(user, remember = True)
    return jsonify(message='logged in Sucess'), 200
  return jsonify(message='log in FAIL'), 200
  

# Mr. Mendez labs

@user_views.route('/identify')
@login_required
def identify_view():
  user = User.query.filter_by(username = current_user.username).first()
  if user:
    return (user.toJSON())
  return jsonify( message='no user found'), 400

@user_views.route('/logout', methods=['GET'])
def logout_action():
  logout_user()
  return jsonify( message='logged out'), 200



@user_views.route('/api/delete/organization/<int:orgId>', methods=['DELETE'])
def delete_organization_action(orgId):
   delete_organization(orgId)
   return jsonify(message="Organization deleted!"), 200
   