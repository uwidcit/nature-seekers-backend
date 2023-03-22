from App.models import Nest
from App.database import db

import json

#Create nest object
def create_nest(num_yolked, num_unyolked, location_name, latitude, longitude, zone, distance_from_vege, distance_from_high_water):
    newnest = Nest(num_yolked=num_yolked, num_unyolked=num_unyolked, location_name=location_name, latitude=latitude, longitude=longitude, zone=zone, distance_from_vege=distance_from_vege, distance_from_high_water=distance_from_high_water)
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