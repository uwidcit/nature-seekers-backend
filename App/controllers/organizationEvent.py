from App.models import OrganizationEvent
from App.database import db

import json

#----------Create organizationEvent object
def create_organizationEvent(organization_id, event_name):
    neworganizationEvent = OrganizationEvent(organization_id=organization_id, event_name=event_name)
    db.session.add(neworganizationEvent)
    db.session.commit()
    return neworganizationEvent

#----------Get organizationEvent by organizationEvent_id
def get_organizationEvent(organizationEvent_id):
    return OrganizationEvent.query.get(organizationEvent_id)

#----------Get all organizationEvents
def get_all_organizationEvent_json():
    organizationEvents = OrganizationEvent.query.all()
    if not organizationEvents:
        return []
    return [organizationEvent.toJSON() for organizationEvent in organizationEvents]

#----------Update organization event name 
def edit_organizationEvent_name(organizationEventid, new_event_name):
    orgEvent = OrganizationEvent.query.filter_by(id=organizationEventid).first()
    if not orgEvent:
        return ["No Organization Event found"]

    orgEvent.event_name = new_event_name
    db.session.add(orgEvent)
    db.session.commit()
    return orgEvent
    
#----------Delete an organizationEvent by excavation_id
def delete_organizationEvent(organizationEvent_id):
    organizationEvent = get_organizationEvent(organizationEvent_id)
    if organizationEvent:
        db.session.delete(organizationEvent)
        return db.session.commit()
    return None