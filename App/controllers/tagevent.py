from App.models import Turtle, User, TagEvent, Contributor
from App.database import db



def create_tag_event (turtleid, contributorid, comments, weight, length, lat, lon):
    
    contributor = Contributor.query.get(contributorid)
    turtle = Turtle.query.get(turtleid)

    
    if contributor and turtle:
        new_tagevent = TagEvent (turtleid=turtleid, contributorid=contributorid, comments=comments, weight=weight, length=length, lat=lat, lon=lon)
        
        db.session.add(new_tagevent)
        db.session.commit()
        
        return new_tagevent
    
    return None
