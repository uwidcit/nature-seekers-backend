from App.database import db
import enum
from datetime import *

class Excavation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    num_yolked = db.Column(db.Integer, nullable=False)
    num_yolkless = db.Column(db.Integer, nullable=False)
    timestamp_excavated =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    timestamp_reburied = db.Column(db.DateTime, nullable=False)
    
    nest = db.relationship("Nest", backref=db.backref("excavations"))


    def toJSON(self):
        return {
            'id': self.id,
            'nest_id': self.nest_id,
            'num_yolked': self.num_yolked,
            'num_yolkless': self.num_yolkless,
            'timestamp_excavated': self.timestamp_excavated.strftime("%Y/%m/%d, %H:%M:%S"),
            'timestamp_reburied': self.timestamp_reburied.strftime("%Y/%m/%d %H:%M")
        }