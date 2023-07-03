from App.models import Excavation
from App.database import db

import json

#Create excavation object
def create_excavation(nest_id):
    newexcavation = Excavation(nest_id=nest_id)
    db.session.add(newexcavation)
    db.session.commit()
    return newexcavation

#Get excavation by excavation_id
def get_excavation(exacavation_id):
    return Excavation.query.get(exacavation_id)

#----------Get turtle Excavation by nest_id
def get_turtleExcavation_by_nest(nest_id):
    turtleExcavations = Excavation.query.filter_by(nest_id=nest_id).all()
    return [turtleExcavation.toJSON() for turtleExcavation in turtleExcavations]


#Get all excavations
def get_all_excavation_json():
    excavations = Excavation.query.all()
    if not excavations:
        return []
    return [excavation.toJSON() for excavation in excavations]

#Delete an excavation by exacavation_id
def delete_excavation(exacavation_id):
    excavation = get_excavation(exacavation_id)
    if excavation:
        db.session.delete(excavation)
        return db.session.commit()
    return None