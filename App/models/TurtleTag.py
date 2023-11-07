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
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.id'))
    status = db.Column(db.Enum(TagStatus))
    location = db.Column(db.Enum(LocationStatus))

    turtle = db.relationship('Turtle', backref=db.backref("tags"))
    tag = db.relationship('Tag', backref=db.backref("detail", uselist=False), uselist=False) # Strict 1 to 1 rel

    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'tag_id': self.tag_id,
            'code': self.tag.code,
            'status': self.status.name,
            'location': self.location.name,
        }
    