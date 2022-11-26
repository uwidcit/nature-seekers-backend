from App.database import db
import enum

class TagStatus(enum.Enum):
    DAMAGED = "damaged"
    REPLACED = "replaced"
    ACTIVE = "active"

class LocationStatus(enum.Enum):
    LEFTFLIPPER = "L-flipper"
    RIGHTFLIPPER = "R-flipper"
    PIT = "Pit"

class TurtleTag(db.Model):
    turtletagid = db.Column(db.Integer, primary_key=True)
    tageventid = db.Column(db.Integer, db.ForeignKey('tagevent.tageventid'))
    code = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(TagStatus))
    location = db.Column(db.Enum(LocationStatus))

    def toJSON(self):
        return {
            'turtletagid': self.turtletagid,
            'tageventid': self.tageventid,
            'code': self.code,
            'status': self.status,
            'location': self.location
        }