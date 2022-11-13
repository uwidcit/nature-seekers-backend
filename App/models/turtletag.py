from App.database import db
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy import PickleType
import enum

class TagStatus(enum.Enum):
    DAMAGED = "damaged"
    REPLACED = "replaced"
    ACTIVE = "active"

class TurtleTag(db.Model):
    turtletagid = db.Column(db.Integer, primary_key=True)
    tageventid = db.relationship(
        "Tag", backref="tagevent", lazy=True, cascade="all, delete-orphan"
    )
    code = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(TagStatus))
    location = db.Column(MutableList.as_mutable(PickleType),
        default=["L-flipper", "R-flipper", "Pit"])