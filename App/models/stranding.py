from App.database import db

class Stranding(db.Model):
    strandingId = db.Column(db.Integer, primary_key=True)
    turtleId = db.Column(db.Integer, db.ForeignKey('turtle.turtleId'))
    userId  = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'strandingId': self.strandingId,
            'turtleId': self.turtleId,
            'userId': self.userId,
            'comments': self.comments,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }