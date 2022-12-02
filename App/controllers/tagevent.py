from App.models import Turtle, User, TagEvent
from App.database import db


def get_turtle (id):
    return Turtle.query.get(id)


def get_user (id):
    return User.query.get(id)


def create_tag_event (turtleid, userid, comments, timestamp, weight, length, lat, lon):
    
    user = get_user (userid)
    turtle = get_turtle (turtleid)
    
    if user and turtle:
        new_tagevent = TagEvent (turtleid=turtleid, userid=userid, comments=comments, timestamp=timestamp, weight=weight, length=length, lat=lat, lon=lon)
        
        db.session.add(new_tagevent)
        db.session.commit()
        
        return new_tagevent
    
    return None
