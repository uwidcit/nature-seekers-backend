from App.models import User, Admin, Citizen ,Organization
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def create_admin(username, password, firstname, lastname, email):
    newuser = Admin(username, password, firstname, lastname, email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except Exception as e:
        print(e)
        return None

def create_organization(username, password, firstname, lastname, email):
    newuser = Organization(username, password, firstname, lastname, email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except Exception as e:
        print(e)
        return None

def create_citizen(username, password, firstname, lastname, email):
    newuser = Citizen(username, password, firstname, lastname, email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except Exception as e:
        print(e)
        return None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_citizen(id):
    return Citizen.query.get(id)

# def is_admin(id):
#     return Admin.query.get(id) !=None

def get_all_admins():
    return Admin.query.all()

def get_all_citizens():
    return Citizen.query.all()

def get_all_organizations():
    return Organization.query.all()

def get_all_citizens_json():
    citizen = Citizen.query.all()
    users = []
    if not (citizen):
        return []
    
    for c in citizen:
        users.append(c.toJSON())
    return users

def get_all_admins_json():
    admin = Admin.query.all()
    users = []
    if not (admin):
        return []
    
    for a in admin:
        users.append(a.toJSON())
    return users

def get_all_organizations_json():
    organization = Organization.query.all()
    users = []
    if not (organization):
        return []
    
    for o in organization:
        users.append(o.toJSON())
    return users

def get_all_users():
    result = get_all_admins()
    result += get_all_citizens()
    return result

def get_all_users_json():
    result = get_all_admins_json()
    result += get_all_citizens_json()
    result += get_all_organizations_json()
    return result
    

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def delete_organization(id):
    organization = Organization.query.get(id)
    if organization:
        db.session.delete(organization)
        return db.session.commit()
    return None

