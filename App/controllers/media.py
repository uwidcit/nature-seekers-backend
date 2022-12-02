from App.models import Media
from App.database import db

import json

def create_media(pictureid, tageventid, filename, url, timestamp):
    new_media = Media(pictureid=pictureid, tageventid=tageventid, filename=filename, url=url, timestamp=timestamp)
    db.session.add(new_media)
    db.session.commit()
    return new_media

# return all media in json format
def get_media_json():
    medias = Media.query.all()
    if not medias:
        return []
    return [media.toJSON() for media in medias]
