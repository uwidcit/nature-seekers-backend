import datetime
from App.database import db

class NestRelocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.nest_id'))

    from_location_name = db.Column(db.String, nullable=False)
    from_latitude = db.Column(db.Float, nullable=False)
    from_longitude = db.Column(db.Float, nullable=False)
    from_zone = db.Column(db.Integer, nullable=False)
    from_distance_from_vege = db.Column(db.Integer, nullable=False)
    from_distance_from_high_water = db.Column(db.Integer, nullable=False)

    to_location_name = db.Column(db.String, nullable=False)
    to_latitude = db.Column(db.Float, nullable=False)
    to_longitude = db.Column(db.Float, nullable=False)
    to_zone = db.Column(db.Integer, nullable=False)
    to_distance_from_vege = db.Column(db.Integer, nullable=False)
    to_distance_from_high_water = db.Column(db.Integer, nullable=False)

    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'nest_id': self.nest_id,

            'from_location_name': self.from_location_name,
            'from_latitude': self.from_latitude,
            'from_longitude': self.from_longitude,
            'from_zone': self.from_zone,
            'from_distance_from_vege': self.from_distance_from_vege,
            'from_distance_from_high_water': self.from_distance_from_high_water,

            'to_location_name': self.to_location_name,
            'to_latitude': self.to_latitude,
            'to_longitude': self.to_longitude,
            'to_zone': self.to_zone,
            'to_distance_from_vege': self.to_distance_from_vege,
            'to_distance_from_high_water': self.to_distance_from_high_water,

            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }