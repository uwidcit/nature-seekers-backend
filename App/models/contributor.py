from App.models import User
from App.database import db

class Contributor(User):

    __tablename__ = 'contributor'

    orgid = db.Column(db.Integer, db.ForeignKey('Organization.orgid'))


    __mapper_args__ = {
        'polymorphic_identity': 'contributor'
    }

    def __init__(self, username, password, firstname, lastname, email):
        super().__init__(username, password, firstname, lastname, email)
    
    def __repr__(self):
        return f'<contributor {self.id} {self.username}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'orgid': self.orgid,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username,
            'type': self.type
        }
