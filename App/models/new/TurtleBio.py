from App.database import db
import datetime

class TurtleBio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.turtle_id'))
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'turtle_id': self.turtle_id,
            'length': self.length,
            'width': self.width,
            'weight': self.weight,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }