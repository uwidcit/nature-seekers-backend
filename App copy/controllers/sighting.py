from App.models import Sighting
from App.database import db

import json

def create_sighting(userId, turtleId, lat, lon, comments):
    newsighting = Sighting(userId=userId, turtleId=turtleId, lat=lat, lon=lon, comments=comments)
    db.session.add(newsighting)
    db.session.commit()
    return newsighting

def get_sighting_by_turtleId(turtleId):
    sightings = Sighting.query.filter_by(turtleId=turtleId).all()
    if not sightings:
        return[]
    return [sighting.toJSON() for sighting in sightings]
    
def get_sighting(sightingid):
    return Sighting.query.get(sightingid)

def get_all_sighting_json():
    sightings = Sighting.query.all()
    if not sightings:
        return []
    return [sighting.toJSON() for sighting in sightings]

def delete_sighting(id):
    sighting = get_sighting(id)
    if sighting:
        db.session.delete(sighting)
        return db.session.commit()
    return None