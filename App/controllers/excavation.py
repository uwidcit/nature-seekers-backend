from App.models import Excavation
from App.database import db

import json

def create_excavation(userid, description, lat, lon):
    newexcavation = Excavation(userid=userid, description=description, lat=lat, lon=lon)
    db.session.add(newexcavation)
    db.session.commit()
    return newexcavation


def get_excavation(exacavationid):
    return Excavation.query.get(exacavationid)

def get_all_excavation_json():
    excavations = Excavation.query.all()
    if not excavations:
        return []
    return [excavation.toJSON() for excavation in excavations]