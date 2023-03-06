from App.models import Capture
from App.database import db

import json

def create_capture(userid, turtleId, timestamp, comments):
    newcapture = Capture(userid=userid, turtleId=turtleId, timestamp=timestamp, comments=comments)
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


    return {
            'captureId': self.captureId,
            'turtleId': self.turtleId,
            'userId': self.userId,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
            'comments': self.comments
        }