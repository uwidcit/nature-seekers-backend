from App.database import db
from datetime import *
import enum

class TurtleEventType(enum.Enum):
    SIGHTING = "sighting"
    STRANDING = "stranding"
    CAPTURE = "capture"
    TAG = "tag"
    INJURY = "injury"

class IsAlive(enum.Enum):
    ALIVE = "alive"
    DEAD = "dead"

class TurtleEvent(db.Model):

    __tablename__ = 'turtleEvent'

    id = db.Column(db.Integer, primary_key=True)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    beach_name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    verified  = db.Column(db.Boolean, nullable=False, default= False)
    event_type = db.Column(db.Enum(TurtleEventType), nullable=True)
    state = db.Column(db.Enum(IsAlive))
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'user_id': self.user_id,
            'beach_name': self.beach_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'verified': self.verified,
            'event_type': self.event_type.name,
            'state':self.state.name,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }