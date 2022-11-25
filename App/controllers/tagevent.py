from App.models import TagEvent
from App.database import db

def create_tag_event (turtleid, userid, comments, timestamp, weight, length, lat, lon):
    new_tagEvent = TagEvent (turtleid=turtleid, userid=userid, comments=comments, timestamp=timestamp, weight=weight, length=length, lat=lat, lon=lon)

    db.session.add(new_tagEvent)
    db.session.commit()

    return new_tagEvent
