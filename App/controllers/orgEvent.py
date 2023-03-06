from App.models import OrgEvent
from App.database import db

import json

def create_orgEvent(userid, description, lat, lon):
    neworgEvent = OrgEvent(userid=userid, description=description, lat=lat, lon=lon)
    db.session.add(neworgEvent)
    db.session.commit()
    return neworgEvent

def get_orgEvent(orgEventid):
    return OrgEvent.query.get(orgEventid)

def get_all_orgEvent_json():
    orgEvents = OrgEvent.query.all()
    if not orgEvents:
        return []
    return [orgEvent.toJSON() for orgEvent in orgEvents]