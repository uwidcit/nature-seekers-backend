from App.models import TurtleActivity
from App.database import db

import json

#Create turtleActivity object
def create_turtleActivity(
                        turtle_id,
                        Activity
                        ):
    
    newturtleActivity = TurtleActivity(
                                        turtle_id,
                                        Activity
                                        )
    
    db.session.add(newturtleActivity)
    db.session.commit()
    return newturtleActivity

#Get turtleActivity by turtleActivity_id
def get_turtleActivity(turtleActivity_id):
    return TurtleActivity.query.get(turtleActivity_id)

#Get all turtleActivitys
def get_all_turtleActivity_json():
    turtleActivitys = TurtleActivity.query.all()
    if not turtleActivitys:
        return []
    return [turtleActivity.toJSON() for turtleActivity in turtleActivitys]
    
#Delete an turtleActivity by excavation_id
def delete_turtleActivity(turtleActivity_id):
    turtleActivity = get_turtleActivity(turtleActivity_id)
    if turtleActivity:
        db.session.delete(turtleActivity)
        return db.session.commit()
    return None