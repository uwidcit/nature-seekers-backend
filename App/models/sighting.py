from App.database import db

class Sighting(db.Model):
    sightingId = db.Column(db.Integer, primary_key=True)
    turtleId = db.Column(db.Integer, db.ForeignKey('turtle.turtleId'))
    userId  = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    lat =  db.Column(db.Float, nullable=False)
    lon =  db.Column(db.Float, nullable=False)
    def toJSON(self):
        return {
            'sightingId': self.sightingId,
            'turtleId': self.turtleId,
            'userId': self.userId,
            'comments': self.comments,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
            'latitude': self.lat,
            'longitude': self.lon
        }