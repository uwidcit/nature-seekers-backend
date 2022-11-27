from App.models import User

class Contributor(User):

    __tablename__ = 'contributor'

    __mapper_args__ = {
        'polymorphic_identity': 'contributor'
    }

    def __init__(self, username, password, firstname="bob", lastname="bob", email="bob@mail.com"):
        super().__init__(username, password, firstname, lastname, email)
    
    def __repr__(self):
        return f'<contributor {self.id} {self.username}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username,
            'type': self.type
        }
