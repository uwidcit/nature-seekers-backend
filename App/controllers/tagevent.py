from App.models import Turtle, User, TagEvent, TurtleTag, Media
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

# return all tagevents in json format
def get_tagevent_json():
    tagevents = TagEvent.query.all()
    if not tagevents:
        return []
    return [tagevent.toJSON() for tagevent in tagevents]


''' do we need 
the tagevent
foreign keys for the 
new object created 
in TUrtleTag and Media? '''
def addTag(code, location):
    if (not code): # code doesn't exist already
        new_turtletag = TurtleTag(code=code, location=location)
        db.session.add(new_turtletag)
        db.session.commit()
        return new_turtletag 

def addMedia(filename, url):
    new_media = Media(filename=filename, url=url)
    db.session.add(new_media)
    db.session.commit()
    return new_media