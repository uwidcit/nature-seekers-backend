from App.models import Stranding
from App.database import db

import json

def create_stranding(userid, description, lat, lon):
    newstranding = Stranding(userid=userid, description=description, lat=lat, lon=lon)
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