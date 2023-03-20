from App.models import Media
from App.database import db

import json

def create_media(tageventid, filename, url):
    new_media = Media(tageventid=tageventid, filename=filename, url=url)
    db.session.add(new_media)
    db.session.commit()
    return new_media


def get_media(pictureid):
    return Media.query.get(pictureid)

# return all media in json format
def get_all_media_json():
    medias = Media.query.all()
    if not medias:
        return []
    return [media.toJSON() for media in medias]

def delete_media(id):
    media = get_media(id)
    if media:
        db.session.delete(media)
        return db.session.commit()
    return None