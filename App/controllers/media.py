from App.models import Media
from App.database import db

import json

def create_media(tageventid, filename, url):
    new_media = Media(tageventid=tageventid, filename=filename, url=url)
    db.session.add(new_media)
    db.session.commit()
    return new_media
