from App.models import TurtleEventMedia
from App.database import db

import json

#Create turtle_event_media object
def create_turtle_event_media(
                    event_id,
                    url,
                    filename
                    ):
    
    newturtle_event_media = TurtleEventMedia(
                    event_id,
                    url,
                    filename
                    )
    
    db.session.add(newturtle_event_media)
    db.session.commit()
    return newturtle_event_media

#Get turtle_event_media by turtle_event_media_id
def get_turtle_event_media(turtle_event_media_id):
    return TurtleEventMedia.query.get(turtle_event_media_id)

#Get all turtle_event_medias
def get_all_turtle_event_media_json():
    turtle_event_medias = TurtleEventMedia.query.all()
    if not turtle_event_medias:
        return []
    return [turtle_event_media.toJSON() for turtle_event_media in turtle_event_medias]
    
#Delete an turtle_event_media by excavation_id
def delete_turtle_event_media(turtle_event_media_id):
    turtle_event_media = get_turtle_event_media(turtle_event_media_id)
    if turtle_event_media:
        db.session.delete(turtle_event_media)
        return db.session.commit()
    return None