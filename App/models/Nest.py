from App.database import db
from datetime import *

class Nest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    zone = db.Column(db.Integer, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    turtle_id = db.Column(db.Integer, db.ForeignKey('turtle.id'), nullable=False)

    turtle = db.relationship('Turtle', backref=db.backref("nests"))

    def toJSON(self):
        return {
            'id': self.id,
            'location_name': self.location_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'zone': self.zone,
            'turtle_id': self.turtle_id,
            'timestamp': self.timestamp.strftime("%d %B %Y"),
        }