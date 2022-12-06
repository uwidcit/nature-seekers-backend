from App.models import Turtle, TagEvent, Contributor
from App.database import db


#def get_turtle (id):
#   return Turtle.query.get(id)

#def get_user (id):
#    return User.query.get(id)

def get_tag_event (tageventid):
    return TagEvent.query.get(tageventid)

def get_all_tag_events():
    return TagEvent.query.all()


def create_tag_event (turtleid, contributorid, comments, weight, length, lat, lon):
    
    #user = get_user (userid)
    #turtle = get_turtle (turtleid)

    contributor = Contributor.get_contributor(contributorid)
    turtle = Turtle.get_turtle(turtleid)
    
    if contributor and turtle:
        new_tagevent = TagEvent (turtleid=turtleid, contributorid=contributorid, comments=comments, weight=weight, length=length, lat=lat, lon=lon)
        
        db.session.add(new_tagevent)
        db.session.commit()
        
        return new_tagevent
    
    return None


def get_all_tag_events_json():
    tag_events = get_all_tag_events()

    if not tag_events:
        return []

    return [tagevent.toJSON() for tagevent in tag_events]
