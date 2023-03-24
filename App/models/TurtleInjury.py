from App.database import db
from datetime import *

class TurtleInjury(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.id'))
    description = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'description': self.description,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }