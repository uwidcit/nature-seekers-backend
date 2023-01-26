from App.database import db
from datetime import datetime

class Excavation(db.Model):
    excavationid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    description =  db.Column(db.String, nullable=False)
    lat =  db.Column(db.Float, nullable=False)
    lon =  db.Column(db.Float, nullable=False)

    def toJSON(self):
        return {
            'excavationid': self.excavationid,
            'userid': self.userid,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
            'description': self.excavationid,
            'latitude': self.lat,
            'longitude': self.lon
        }