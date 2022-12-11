from App.database import db
from datetime import datetime

class TagEvent(db.Model):
    __tablename__ = 'tagevent'
    tageventid = db.Column(db.Integer, primary_key=True)
    turtleid = db.Column(db.Integer, db.ForeignKey('turtle.turtleid'))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments =  db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    weight =  db.Column(db.Integer, nullable=False)
    length =  db.Column(db.Integer, nullable=False)
    lat =  db.Column(db.Float, nullable=False)
    lon =  db.Column(db.Float, nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    def toJSON(self):
        return {
            'tageventid': self.tageventid,
            'turtleid': self.turtleid,
            'userid': self.userid,
            'comments': self.comments,
            'timestamp': self.timestamp,
            'weight': self.weight,
            'length': self.length,
            'latitude': self.lat,
            'longitude': self.lon,
            'approved': self.approved
        }