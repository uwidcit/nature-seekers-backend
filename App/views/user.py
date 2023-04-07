from functools import wraps
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, set_access_cookies, set_refresh_cookies
from flask_login import current_user, login_required, login_user, logout_user

from App.models import User, Admin, Citizen, Organization


from App.controllers import (
    create_citizen,
    create_admin,
    create_organization,
    get_all_users,
    get_all_users_json,
    get_all_organizations_json,
    delete_organization
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# ----------Decorators to limit user permissions


def citizen_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Citizen):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper


def organization_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Organization):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Admin):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper


# ------------Get All Users
@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)


# ---------Create users
@user_views.route('/api/citizens', methods=['POST'])
def create_citizen_action():
    data = request.json
    res = create_citizen(data['username'], data['password'],
                         data['firstname'], data['lastname'], data['email'])
    if res:
        return jsonify({'message': f"citizen user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401


@user_views.route('/api/organization', methods=['POST'])
def create_organization_action():
    data = request.json
    res = create_organization(
        data['username'], data['password'], data['firstname'], data['lastname'], data['email'])
    if res:
        return jsonify({'message': f"organization user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401


@user_views.route('/api/admins', methods=['POST'])
def create_admin_action():
    data = request.json
    res = create_admin(data['username'], data['password'],
                       data['firstname'], data['lastname'], data['email'])
    if res:
        return jsonify({'message': f"admin user {data['username']} created"}), 201
    return jsonify({'message': f"error creating user"}), 401

# -----------Login Users


@user_views.route('/login', methods=['POST'])
def login_view():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # Create the tokens we will be sending back to the user
        access_token = create_access_token(identity=username)

        # Set the JWT cookies in the response
        resp = jsonify({'message': 'Logged in successfully'})
        set_access_cookies(resp, access_token)
        #return resp, 200
        return jsonify(message='Logged-in Sucessfully'), 200
    return jsonify(message='Log in Failed'), 400



# ------------ Identify logged in User


@user_views.route('/identify')
def identify_view():
    user = User.query.filter_by(username=current_user.username).first()
    if user:
        return (user.toJSON())
    return jsonify(message='no user found'), 400

# ---------------Log out User


@user_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    return jsonify(message='logged out'), 200

# ---------------Get All Organizations


@user_views.route('/api/organization', methods=['GET'])
def get_all_organizations_action():
    organizations = get_all_organizations_json()
    return jsonify(organizations)

# -----------------Delete Organization


@user_views.route('/api/delete/organization/<int:orgId>', methods=['DELETE'])
def delete_organization_action(orgId):
    delete_organization(orgId)
    return jsonify(message="Organization deleted!"), 200
