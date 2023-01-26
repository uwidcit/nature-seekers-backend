import flask_login
from flask_jwt_extended import JWTManager
from App.models import User, Admin, Contributor


# Authenticate Admins / Contributors
def authenticate(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if admin and admin.check_password(password):
        return admin
    contributor = Contributor.query.filter_by(username=username).first()
    if contributor and contributor.check_password(password):
        return contributor
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    admin = Admin.query.get(payload['identity'])
    if admin:
        return admin
    contributor = Contributor.query.get(payload['identity'])
    if contributor:
        return contributor
    return None

def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)

def logout_user():
    flask_login.logout_user()

def setup_jwt(app):
    return JWTManager(app)