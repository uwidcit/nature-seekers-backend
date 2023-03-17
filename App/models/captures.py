from App.database import db
from datetime import datetime

class Captures(db.Model):
    captureId = db.Column(db.Integer, primary_key=True)
    turtleId = db.Column(db.Integer, db.ForeignKey('turtle.turtleid'))
    userId  = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'captureId': self.captureId,
            'turtleId': self.turtleId,
            'userId': self.userId,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
            'comments': self.comments
        }