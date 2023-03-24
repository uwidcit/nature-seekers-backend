from App.models import TurtleEventMedia
from App.database import db

import json

#Create turtleEventMedia object
def create_turtleEventMedia(
                    event_id,
                    url,
                    filename
                    ):
    
    newturtleEventMedia = TurtleEventMedia(
                    event_id=event_id,
                    url=url,
                    filename=filename
                    )
    
    db.session.add(newturtleEventMedia)
    db.session.commit()
    return newturtleEventMedia

#Get turtleEventMedia by turtleEventMedia_id
def get_turtleEventMedia(turtleEventMedia_id):
    return TurtleEventMedia.query.get(turtleEventMedia_id)

#Get all turtleEventMedias
def get_all_turtleEventMedia_json():
    turtleEventMedias = TurtleEventMedia.query.all()
    if not turtleEventMedias:
        return []
    return [turtleEventMedia.toJSON() for turtleEventMedia in turtleEventMedias]
    
#Delete an turtleEventMedia by excavation_id
def delete_turtleEventMedia(turtleEventMedia_id):
    turtleEventMedia = get_turtleEventMedia(turtleEventMedia_id)
    if turtleEventMedia:
        db.session.delete(turtleEventMedia)
        return db.session.commit()
    return None