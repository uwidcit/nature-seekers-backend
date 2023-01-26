from App.models import Contributor
from App.database import db

class Organization(db.Model):
    __tablename__ = "Organization"

    orgid = db.Column(db.Integer, primary_key=True)
    description =  db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    phone =  db.Column(db.String, nullable=False)
    website =  db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            'orgid': self.orgid,
            'description': self.description,
            'email': self.email,
            'phone': self.phone,
            'website': self.website
        }