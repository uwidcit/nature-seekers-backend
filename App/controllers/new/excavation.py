from App.models import Excavation
from App.database import db

import json

#Create excavation object
def create_excavation(nest_id):
    newexcavation = Excavation(nest_id)
    db.session.add(newexcavation)
    db.session.commit()
    return newexcavation

#Get excavation by excavation_id
def get_excavation(exacavation_id):
    return Excavation.query.get(exacavation_id)

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