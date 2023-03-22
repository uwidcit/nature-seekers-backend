from App.database import db
import datetime

class TurtleEventMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('turtleevent.event_id'))
    url = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'event_id': self.tevent_id,
            'url': self.url,
            'filename': self.filename,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }