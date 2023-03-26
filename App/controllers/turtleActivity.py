from App.models import TurtleActivity
from App.database import db

import json

#Create turtleActivity object
def create_turtleActivity(
                        turtle_id,
                        activity
                        ):
    
    newturtleActivity = TurtleActivity(
                                        turtle_id=turtle_id,
                                        activity=activity
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


#Update organization event name 
def edit_turtleActivity(turtleActivityid, activity):
    turtleActivity = TurtleActivity.query.filter_by(id=turtleActivityid).first()
    if not turtleActivity:
        return ["No turtle Activity found"]

    turtleActivity.activity = activity
    db.session.add(turtleActivity)
    db.session.commit()
    return turtleActivity