from App.database import db
from datetime import datetime

class Media(db.Model):
    pictureid = db.Column(db.Integer, primary_key=True)
    tageventid = db.Column(db.Integer, db.ForeignKey('tagevent.tageventid'))
    filename = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def toJSON(self):
        return {
            'pictureid': self.pictureid,
            'tageventid': self.tageventid,
            'filename': self.filename,
            'url': self.url,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }