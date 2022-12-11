from App.models import User, Admin, Contributor, TagEvent
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def create_admin(username, password, firstname=None, lastname=None, email=None):
    newuser = Admin(username, password)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except Exception as e:
        print(e)
        return None

def create_contributor(username, password, firstname=None, lastname=None, email=None):
    newuser = Contributor(username, password)
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

def get_contributor(id):
    return Contributor.query.get(id)

# def is_admin(id):
#     return Admin.query.get(id) !=None

def get_all_admins():
    return Admin.query.all()

def get_all_contributors():
    return Contributor.query.all()

def get_all_contributors_json():
    contributor = Contributor.query.all()
    users = []
    if not (contributor):
        return []
    
    for c in contributor:
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

def get_all_users():
    result = get_all_admins()
    result += get_all_contributors()
    return result

def get_all_users_json():
    result = get_all_admins_json()
    result += get_all_contributors_json()
    return result
    

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def approve(tagEventId):
    tagevent = TagEvent.query.get(tagEventId)
    if (tagevent):
        tagevent.approved = True
        return tagevent