from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

##stuff for identify
from App.models import User, Admin, Contributor, TagEvent


from App.controllers import (
    create_contributor,
    create_admin, 
    get_all_users,
    get_all_users_json,
    admin_login,
    contributor_login
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

@user_views.route('/api/contributors', methods=['POST'])
def create_contributor_action():
    data = request.json
    res = create_contributor(data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res: 
        return jsonify({'message': f"contributor user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401

@user_views.route('/api/admins', methods=['POST'])
def create_admin_action():
    data = request.json
    res = create_admin(data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res: 
        return jsonify({'message': f"admin user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401


'''
@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    current_identity = get_jwt_identity()
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})
'''

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


#Login Users
@user_views.route('/login/admin', methods=['POST'])
def admin_login_view():
  data = request.json
  token = admin_login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)

@user_views.route('/login/contributor', methods=['POST'])
def contributor_login_view():
  data = request.json
  token = contributor_login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)


# Mr. Mendez labs

@user_views.route('/identify')
@jwt_required()
def identify_view():
  username = get_jwt_identity() # convert sent token to user name
  #retrieve regular user with given username
  contributor = Contributor.query.filter_by(username=username).first()
  if contributor:
    return jsonify(contributor.toJSON()) #jsonify user object
  #retrieve admin user with given username
  admin = Admin.query.filter_by(username=username).first()
  if admin:
    return jsonify(admin.toJSON())#jsonify admin object
