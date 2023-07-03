from App.models import User
from App.database import db

class Organization(User):

    __tablename__ = 'organization'

    __mapper_args__ = {
        'polymorphic_identity': 'organization'
    }

    def __init__(self, username, password, firstname, lastname, email):
        super().__init__(username, password, firstname, lastname, email)
    
    def __repr__(self):
        return f'<organization {self.id} {self.username}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username,
            'type': self.type
        }
