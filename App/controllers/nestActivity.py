from App.models import NestActivity
from App.database import db

import json

#----------Create nestActivity object
def create_nestActivity(nest_id, name, timestamp):
    newnestActivity = NestActivity(nest_id=nest_id, name=name, timestamp=timestamp)
    db.session.add(newnestActivity)
    db.session.commit()
    return newnestActivity

#----------Get nestActivity by nestActivity_id
def get_nestActivity(nestActivity_id):
    return NestActivity.query.get(nestActivity_id)

#----------Get all nestActivitys
def get_all_nestActivity_json():
    nestActivitys = NestActivity.query.all()
    if not nestActivitys:
        return []
    return [nestActivity.toJSON() for nestActivity in nestActivitys]

#----------Get turtle Activity by nest_id
def get_turtleActivity_by_nest(nest_id):
    turtleActivitys = NestActivity.query.filter_by(nest_id=nest_id).all()
    return [turtleActivity.toJSON() for turtleActivity in turtleActivitys]


#----------Delete an nestActivity by nest_id
def delete_nestActivity(nestActivity_id):
    nestActivity = get_nestActivity(nestActivity_id)
    if nestActivity:
        db.session.delete(nestActivity)
        return db.session.commit()
    return None

#----------Update a nestActivity
def update_nestActivity(nestActivity_id, Activity):

    nestActivity = get_nestActivity(nestActivity_id)
    
    if not nestActivity:
        return []
    
    nestActivity.Activity = Activity
   
    db.session.add(nestActivity)
    db.session.commit()
    
    return nestActivity
