from App.models import NestOutcome
from App.database import db

import json

#----------Create nestOutcome object
def create_nestOutcome(nest_id, outcome):
    newnestOutcome = NestOutcome(nest_id=nest_id, outcome=outcome)
    db.session.add(newnestOutcome)
    db.session.commit()
    return newnestOutcome

#----------Get nestOutcome by nestOutcome_id
def get_nestOutcome(nestOutcome_id):
    return NestOutcome.query.get(nestOutcome_id)

#----------Get all nestOutcomes
def get_all_nestOutcome_json():
    nestOutcomes = NestOutcome.query.all()
    if not nestOutcomes:
        return []
    return [nestOutcome.toJSON() for nestOutcome in nestOutcomes]

#----------Delete an nestOutcome by excavation_id
def delete_nestOutcome(nestOutcome_id):
    nestOutcome = get_nestOutcome(nestOutcome_id)
    if nestOutcome:
        db.session.delete(nestOutcome)
        return db.session.commit()
    return None

#----------Update a nestOutcome
def update_nestOutcome(nestOutcome_id, outcome):

    nestOutcome = get_nestOutcome(nestOutcome_id)
    
    if not nestOutcome:
        return []
    
    nestOutcome.outcome = outcome
   
    db.session.add(nestOutcome)
    db.session.commit()
    
    return nestOutcome
