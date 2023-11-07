from App.database import db
import enum
from datetime import *

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, index=True) #Client may have different identifiers other than out autoincrement PK. They need the ability to enter this

    def toJSON(self):
        return {
            'id': self.id,
            'code': self.code,
            'is_assigned': self.detail is not None
        }
    