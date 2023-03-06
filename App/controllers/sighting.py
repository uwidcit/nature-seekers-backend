from App.models import Sighting
from App.database import db

import json

def create_sighting(userid, turtleId, lat, lon, timestamp):
    newsighting = Sighting(userid=userid, turtleId=turtleId, lat=lat, lon=lon, comments=comments, timestamp=timestamp)
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