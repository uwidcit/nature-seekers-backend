from App.database import db

class Media(db.Model):
    pictureid = db.Column(db.Integer, primary_key=True)
    tageventid = db.Column(db.Integer, db.ForeignKey('tagevent.tageventid'))
    filename = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def toJSON(self):
        return {
            'pictureid': self.pictureid,
            'tageventid': self.tageventid,
            'filename': self.filename,
            'url': self.url,
            'timestamp': self.timestamp,
        }