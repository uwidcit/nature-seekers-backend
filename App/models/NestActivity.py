from datetime import *
from App.database import db

class NestActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))

    name = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    nest = db.relationship("Nest", backref=db.backref("activities"))
    
    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'nest_id': self.nest_id,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),
        }