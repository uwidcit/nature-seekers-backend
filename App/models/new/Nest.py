from App.database import db
import datetime

class Nest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_yolked = db.Column(db.Integer, nullable=False)
    num_unyolked = db.Column(db.Integer, nullable=False)
    location_name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    zone = db.Column(db.Integer, nullable=False)
    distance_from_vege = db.Column(db.Integer, nullable=False)
    distance_from_high_water = db.Column(db.Integer, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'num_yolked': self.num_yolked,
            'num_unyolked': self.num_unyolked,
            'location_name': self.location_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'zone': self.zone,
            'distance_from_vege': self.distance_from_vege,
            'distance_from_high_water': self.distance_from_high_water,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }