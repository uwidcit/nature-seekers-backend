from App.database import db

class Excavation(db.Model):
    excavationid = db.Column(db.Integer, primary_key=True)
    userid = db.relationship(
        "User", backref="excavation", lazy=True, cascade="all, delete-orphan"
    )
    details =  db.Column(db.String, nullable=False)