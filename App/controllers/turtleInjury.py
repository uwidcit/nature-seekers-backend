from App.models import TurtleInjury
from App.database import db

import json

#----------Create turtleInjury object
def create_turtleInjury(
                    turtle_id,
                    description
                    ):
    
    newturtleInjury = TurtleInjury(
                    turtle_id=turtle_id,
                    description=description
                    )
    
    db.session.add(newturtleInjury)
    db.session.commit()
    return newturtleInjury

#----------Get turtleInjury by turtleInjury_id
def get_turtleInjury(turtleInjury_id):
    return TurtleInjury.query.get(turtleInjury_id)

#----------Get all turtleInjurys
def get_all_turtleInjury_json():
    turtleInjurys = TurtleInjury.query.all()
    if not turtleInjurys:
        return []
    return [turtleInjury.toJSON() for turtleInjury in turtleInjurys]
    
#----------Get turtle Injury by turtle_id
def get_turtleInjury_by_turtle(turtle_id):
    turtleInjurys = TurtleInjury.query.filter_by(turtle_id=turtle_id).all()
    return [turtleInjury.toJSON() for turtleInjury in turtleInjurys]

#----------Delete an turtleInjury by excavation_id
def delete_turtleInjury(turtleInjury_id):
    turtleInjury = get_turtleInjury(turtleInjury_id)
    if turtleInjury:
        db.session.delete(turtleInjury)
        return db.session.commit()
    return None

#----------Update organization event name 
def edit_turtleInjury(turtleInjuryid, description):
    turtleInjury = TurtleInjury.query.filter_by(id=turtleInjuryid).first()
    if not turtleInjury:
        return ["No Turtle Injury found"]

    turtleInjury.description = description
    db.session.add(turtleInjury)
    db.session.commit()
    return turtleInjury