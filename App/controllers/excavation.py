from App.models import Excavation
from App.database import db
from App.config import config
import json

def create_excavation(excavationid, userid, timestamp, description, lat, long):
    newexcavation = Excavation(excavationid=excavationid, userid=userid, timestamp=timestamp, description=description, lat=lat, long=long)
    db.session.add(newexcavation)
    db.session.commit()
    return newexcavation
