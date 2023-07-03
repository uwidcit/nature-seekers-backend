from App.models import TurtleBio
from App.database import db

import json

#----------Create turtle_bio object
def create_turtleBio(
                    turtle_id,
                    length,
                    width,
                    weight
                    ):
    
    newturtle_bio = TurtleBio(
                    turtle_id=turtle_id,
                    length=length,
                    width=width,
                    weight=weight
                    )
    
    db.session.add(newturtle_bio)
    db.session.commit()
    return newturtle_bio

#----------Get turtle_bio by turtle_bio_id
def get_turtleBio(turtle_bio_id):
    return TurtleBio.query.get(turtle_bio_id)

#----------Get turtle bio by turtle_id
def get_turtleBio_by_turtle(turtle_id):
    turtleBios = TurtleBio.query.filter_by(turtle_id=turtle_id).all()
    return [turtleBio.toJSON() for turtleBio in turtleBios]

#----------Get all turtle_bios
def get_all_turtleBio_json():
    turtle_bios = TurtleBio.query.all()
    if not turtle_bios:
        return []
    return [turtle_bio.toJSON() for turtle_bio in turtle_bios]
    
#----------Delete an turtle_bio by excavation_id
def delete_turtleBio(turtle_bio_id):
    turtle_bio = get_turtleBio(turtle_bio_id)
    if turtle_bio:
        db.session.delete(turtle_bio)
        return db.session.commit()
    return None