from App.models import Stranding
from App.database import db

import json

def create_stranding(userId, turtleId, comments):
    newstranding = Stranding(userId=userId, turtleId=turtleId, comments=comments)
    db.session.add(newstranding)
    db.session.commit()
    return newstranding


def get_stranding(strandingid):
    return Stranding.query.get(strandingid)

def get_all_stranding_json():
    strandings = Stranding.query.all()
    if not strandings:
        return []
    return [stranding.toJSON() for stranding in strandings]

def delete_stranding(id):
    stranding = get_stranding(id)
    if stranding:
        db.session.delete(stranding)
        return db.session.commit()
    return None