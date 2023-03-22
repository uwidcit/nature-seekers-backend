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
                    state
                    ):
    
    newturtleEvent = TurtleEvent(
                    turtle_id,
                    user_id,
                    beach_name,
                    latitude,
                    longitude,
                    verified,
                    event_type,
                    state
                    )
    
    db.session.add(newturtleEvent)
    db.session.commit()
    return newturtleEvent

#Get turtleEvent by turtleEvent_id
def get_turtleEvent(turtleEvent_id):
    return TurtleEvent.query.get(turtleEvent_id)

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