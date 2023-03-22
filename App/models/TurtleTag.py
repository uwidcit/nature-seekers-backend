from App.database import db
import enum
from datetime import *

class TagStatus(enum.Enum):
    DAMAGED = "damaged"
    REPLACED = "replaced"
    ACTIVE = "active"

class LocationStatus(enum.Enum):
    LEFTFLIPPER = "L-flipper"
    RIGHTFLIPPER = "R-flipper"
    PIT = "Pit"

class TurtleTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.turtle_id'))
    status = db.Column(db.Enum(TagStatus))
    location = db.Column(db.Enum(LocationStatus))

    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'status': self.status.name,
            'location': self.location.name
        }
    