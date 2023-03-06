from App.models import Sighting
from App.database import db

import json

def create_sighting(userid, description, lat, lon):
    newsighting = Sighting(userid=userid, description=description, lat=lat, lon=lon)
    db.session.add(newsighting)
    db.session.commit()
    return newsighting


def get_sighting(sightingid):
    return Sighting.query.get(sightingid)

def get_all_sighting_json():
    sightings = Sighting.query.all()
    if not sightings:
        return []
    return [sighting.toJSON() for sighting in sightings]