from App.database import db
from datetime import *

class OrganizationEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_name = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'organization_id': self.organization_id,
            'event_name': self.event_name,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }