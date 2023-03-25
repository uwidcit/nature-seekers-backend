from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import logout_user

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
  print(data['username'], data['password'])
  token = login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password givennn'), 401
  return jsonify(access_token=token)

# Mr. Mendez labs

@user_views.route('/identify')
@jwt_required()
def identify_view():
  username = get_jwt_identity() # convert sent token to user name
  #retrieve regular user with given username
  citizen = Citizen.query.filter_by(username=username).first()
  if citizen:
    return jsonify(citizen.toJSON()) #jsonify user object
  #retrieve admin user with given username
  admin = Admin.query.filter_by(username=username).first()
  if admin:
    return jsonify(admin.toJSON())#jsonify admin object


@user_views.route('/logout', methods=['GET'])
def logout_action():

  return jsonify( message='logged out'), 200
