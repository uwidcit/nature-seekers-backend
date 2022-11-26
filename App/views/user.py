from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    create_contributor,
    create_admin, 
    get_all_users,
    get_all_users_json,
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

@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')