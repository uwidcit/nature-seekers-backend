from App.models import Excavation
from App.database import db

import json

def create_excavation(userid, description, lat, long):
    newexcavation = Excavation(userid=userid, description=description, lat=lat, long=long)
    db.session.add(newexcavation)
    db.session.commit()
    return newexcavation
