from App.models import Nest
from App.database import db

import json

#Create nest object
def create_nest(location_name,latitude,longitude,zone,turtle_id,):
    newnest = Nest(location_name=location_name, latitude=latitude, longitude=longitude, zone=zone, turtle_id=int(turtle_id))
    db.session.add(newnest)
    db.session.commit()
    return newnest

#Get nest by nest_id
def get_nest(nest_id):
    return Nest.query.get(nest_id)

#Get all nests
def get_all_nests_json():
    nests = Nest.query.all()
    if not nests:
        return []
    return [nest.toJSON() for nest in nests]

#Delete an nest by excavation_id
def delete_nest(nest_id):
    nest = get_nest(nest_id)
    if nest:
        db.session.delete(nest)
        return db.session.commit()
    return None

# Update a nest
def update_nest( nest_id,location_name,latitude,longitude,zone,turtle_id,):

    nest = get_nest(nest_id)
    
    if nest:
        nest.nest_id = nest_id
        nest.location_name = location_name
        nest.latitude = latitude
        nest.longitude = longitude
        nest.zone = zone
        nest.turtle_id = turtle_id
        db.session.add(nest)
        db.session.commit()
        
        return nest
