from App.models import Capture
from App.database import db

import json

def create_capture(userid, description, lat, lon):
    newcapture = Capture(userid=userid, description=description, lat=lat, lon=lon)
    db.session.add(newcapture)
    db.session.commit()
    return newcapture


def get_capture(captureid):
    return Capture.query.get(captureid)

def get_all_capture_json():
    captures = Capture.query.all()
    if not captures:
        return []
    return [capture.toJSON() for capture in captures]