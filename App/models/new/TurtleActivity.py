from App.database import db
import enum
import datetime

class Activity(enum.Enum):
    APPROACHING = "approaching"
    BODY_PITTING = "body_pitting"
    COVERING = "covering"
    DIGGING = "digging"
    LAYING = "laying"
    CAMOUFLAGING = "camouflaging"
    LEAVING = "leaving"
    UNKNOWN = "unknown"
    GONE = "gone"

class TurtleActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.turtle_id'))
    activity = db.Column(db.Enum(Activity))
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'activity': self.activity.name,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }