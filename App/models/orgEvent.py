from App.database import db
from datetime import datetime
class OrgEvent(db.Model):
    orgEventId = db.Column(db.Integer, primary_key=True)
    organizationId = db.Column(db.Integer, db.ForeignKey('organization.orgid'))
    userId  = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String, nullable=False)
    time = db.Column(db.Date, nullable=False)
    location = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def toJSON(self):
        return {
            'orgEventId': self.orgEventId,
            'organizationId': self.organizationId,
            'userId': self.userId,
            'name': self.name,
            'time': self.time,
            'location': self.location,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S"),

        }