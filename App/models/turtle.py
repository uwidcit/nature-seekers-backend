from App.database import db

class Turtle(db.Model):
    turtleid = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    sex =  db.Column(db.String, nullable=False)
    DOB =  db.Column(db.Date, nullable=False)