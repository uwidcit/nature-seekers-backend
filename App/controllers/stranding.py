from App.models import Stranding
from App.database import db

import json

def create_stranding(userid, turtleId, comments):
    newstranding = Stranding(userid=userid, turtleId=turtleId, comments=comments)
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