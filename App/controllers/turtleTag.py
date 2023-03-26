from App.models import TurtleTag
from App.database import db

import json

#Create turtleTag object
def create_turtleTag(
                    turtle_id,
                    status,
                    location
                    ):
    
    newturtleTag = TurtleTag(
                    turtle_id=turtle_id,
                    status=status,
                    location=location
                    )
    
    db.session.add(newturtleTag)
    db.session.commit()
    return newturtleTag

#Get turtleTag by turtleTag_id
def get_turtleTag(turtleTag_id):
    return TurtleTag.query.get(turtleTag_id)

#Get all turtleTags
def get_all_turtleTag_json():
    turtleTags = TurtleTag.query.all()
    if not turtleTags:
        return []
    return [turtleTag.toJSON() for turtleTag in turtleTags]
    
#Delete an turtleTag by excavation_id
def delete_turtleTag(turtleTag_id):
    turtleTag = get_turtleTag(turtleTag_id)
    if turtleTag:
        db.session.delete(turtleTag)
        return db.session.commit()
    return None


#Update organization event name 
def edit_turtleTag(turtleTagid, status):
    turtleTag = TurtleTag.query.filter_by(id=turtleTagid).first()
    if not turtleTag:
        return ["No Turtle Injury found"]

    turtleTag.status = status
    db.session.add(turtleTag)
    db.session.commit()
    return turtleTag