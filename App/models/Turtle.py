from App.database import db
import enum

class Sex(enum.Enum):
    MALE = "male"
    FEMALE = "female"

class Species(enum.Enum):
    GREEN = "green"
    HAWKSBILL = "hawksbill"
    LEATHERBACK = "leatherback"
    OTHER = "other"
    

class Turtle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex = db.Column(db.Enum(Sex))
    dob = db.Column(db.Date, nullable=False)
    species = db.Column(db.Enum(Species))

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex.name,
            'dateofbirth': self.dob,
            'species': self.species.name
        }