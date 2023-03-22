from App.database import db
import enum
from datetime import *

class Excavation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.nest_id'))
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def toJSON(self):
        return {
            'id': self.id,
            'nest_id': self.nest_id,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }