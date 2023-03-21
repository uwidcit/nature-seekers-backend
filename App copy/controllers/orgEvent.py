from App.models import OrgEvent
from App.database import db

import json

def create_orgEvent(userId, organizationId, name, time, location):
    neworgEvent = OrgEvent(userId=userId, organizationId=organizationId, name=name, time=time, location=location)
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


def delete_orgEvent(id):
    orgEvent = get_orgEvent(id)
    if orgEvent:
        db.session.delete(orgEvent)
        return db.session.commit()
    return None