from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String, nullable=False)
    lastname =  db.Column(db.String, nullable=False)
    username =  db.Column(db.String, nullable=False, unique=True)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        "polymorphic_on": 'type'
    }

    def __init__(self, username, password, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

