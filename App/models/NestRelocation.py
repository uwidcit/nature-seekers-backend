from datetime import *
from App.database import db

class NestRelocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    to_location_name = db.Column(db.String, nullable=False)
    to_latitude = db.Column(db.Float, nullable=False)
    to_longitude = db.Column(db.Float, nullable=False)
    to_zone = db.Column(db.Integer, nullable=False)

    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    nest = db.relationship("Nest", backref=db.backref("relocations"))

    def toJSON(self):
        return {
            'id': self.id,
            'nest_id': self.nest_id,

            'to_location_name': self.to_location_name,
            'to_latitude': self.to_latitude,
            'to_longitude': self.to_longitude,
            'to_zone': self.to_zone,

            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }