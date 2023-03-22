from App.models import TurtleInjuries
from App.database import db

import json

#Create turtleInjury object
def create_turtleInjury(
                    turtle_id,
                    description
                    ):
    
    newturtleInjury = TurtleInjury(
                    turtle_id,
                    description
                    )
    
    db.session.add(newturtleInjury)
    db.session.commit()
    return newturtleInjury

#Get turtleInjury by turtleInjury_id
def get_turtleInjury(turtleInjury_id):
    return TurtleInjury.query.get(turtleInjury_id)

#Get all turtleInjurys
def get_all_turtleInjury_json():
    turtleInjurys = TurtleInjury.query.all()
    if not turtleInjurys:
        return []
    return [turtleInjury.toJSON() for turtleInjury in turtleInjurys]
    
#Delete an turtleInjury by excavation_id
def delete_turtleInjury(turtleInjury_id):
    turtleInjury = get_turtleInjury(turtleInjury_id)
    if turtleInjury:
        db.session.delete(turtleInjury)
        return db.session.commit()
    return None