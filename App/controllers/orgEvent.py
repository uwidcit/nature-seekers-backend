from App.models import OrgEvent
from App.database import db

import json

def create_orgEvent(userid, organizationId, sex, name, time, location, timestamp):
    neworgEvent = OrgEvent(userid=userid, organizationId=organizationId, sex=sex, name=name, time=time, location=location, timestamp=timestamp)
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
