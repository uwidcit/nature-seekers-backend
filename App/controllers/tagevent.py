
from App.models import Turtle, TagEvent, Contributor, TurtleTag, Media
from App.database import db


#def get_turtle (id):
#   return Turtle.query.get(id)

#def get_user (id):
#    return User.query.get(id)

def get_tag_event (tageventid):
    return TagEvent.query.get(tageventid)

def get_all_tag_events():
    return TagEvent.query.all()

def create_tag_event (turtleid, userid, comments, weight, length, lat, lon, approved):
    
    contributor = Contributor.query.get(userid)
    turtle = Turtle.query.get(turtleid)
    
    if(approved == "True"):
        apppr=True
    else : appr = False

    if contributor and turtle:
        new_tagevent = TagEvent (turtleid=turtleid, userid=userid, comments=comments, weight=weight, length=length, lat=lat, lon=lon, approved = appr)
        
        db.session.add(new_tagevent)
        db.session.commit()
        
        return new_tagevent
    
    return None



def get_all_tag_events_json():
    tag_events = get_all_tag_events()

    if not tag_events:
        return []

    return [tagevent.toJSON() for tagevent in tag_events]

def get_tag_eventID (tageventid):
    return TagEvent.query.get(tageventid)

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
in TUrtleTag and Media? - YES
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
'''
