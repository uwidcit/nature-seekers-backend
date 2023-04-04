from App.models import TurtleEvent
from App.database import db

import json

#Create turtleEvent object
def create_turtleEvent(
                    turtle_id,
                    user_id,
                    beach_name,
                    latitude,
                    longitude,
                    verified,
                    event_type,
                    isAlive
                    ):
    
    newturtleEvent = TurtleEvent(
                    turtle_id=turtle_id,
                    user_id=user_id,
                    beach_name=beach_name,
                    latitude=latitude,
                    longitude=longitude,
                    verified=verified,
                    event_type=event_type,
                    state=isAlive
                    )
    
    db.session.add(newturtleEvent)
    db.session.commit()
    return newturtleEvent

#Get turtleEvent by turtleEvent_id
def get_turtleEvent(turtleEvent_id):
    return TurtleEvent.query.get(turtleEvent_id)

#Get turtle event by turtle_id
def get_turtleEvent_by_turtle(turtle_id):
    turtleEvents = TurtleEvent.query.filter_by(turtle_id=turtle_id).all()
    return [turtleEvent.toJSON() for turtleEvent in turtleEvents]

#Get all turtleEvents by type
def get_all_turtleEvent_by_type_json(type):
    turtleEvents = TurtleEvent.query.filter_by(event_type = type )
    if not turtleEvents:
        return []
    return [turtleEvent.toJSON() for turtleEvent in turtleEvents]
    

#Get all turtleEvents
def get_all_turtleEvent_json():
    turtleEvents = TurtleEvent.query.all()
    if not turtleEvents:
        return []
    return [turtleEvent.toJSON() for turtleEvent in turtleEvents]
    
#Delete an turtleEvent by excavation_id
def delete_turtleEvent(turtleEvent_id):
    turtleEvent = get_turtleEvent(turtleEvent_id)
    if turtleEvent:
        db.session.delete(turtleEvent)
        return db.session.commit()
    return None

#Approve Turtle event -update verified attribute
def approve(turtleEventId):
    turtleEvent = TurtleEvent.query.get(turtleEventId)
    if (turtleEvent):
        turtleEvent.verified = True
        db.session.add(turtleEvent)
        return db.session.commit()
    

# Update a turtleEvent
def update_turtleEvent(
                turtleEvent_id, 
                turtle_id,
                user_id,
                beach_name,
                latitude,
                longitude,
                event_type,
                isAlive,
                ):

    turtleEvent = get_turtleEvent(turtleEvent_id)
    
    if not turtleEvent:
        return []
    
    turtleEvent.turtle_id = turtle_id
    turtleEvent.user_id = user_id
    turtleEvent.beach_name = beach_name
    turtleEvent.latitude = latitude
    turtleEvent.longitude = longitude
    turtleEvent.event_type  = event_type
    turtleEvent.isAlive = isAlive
    
    db.session.add(turtleEvent)
    db.session.commit()
    
    return turtleEvent


#Get Unverified Turtle Events
def get_unverified_turtleEvents():
    turtleEvents=TurtleEvent.query.filter_by(verified = False)
    if not turtleEvents:
        return []
    return [turtleEvent.toJSON() for turtleEvent in turtleEvents]