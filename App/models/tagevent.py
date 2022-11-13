from App.database import db

class TagEvent(db.Model):
    turtleEventid = db.Column(db.Integer, primary_key=True)
    tagid = db.relationship(
        "Tag", backref="tagevent", lazy=True, cascade="all, delete-orphan"
    )
    turtleid = db.relationship(
        "Turtle", backref="tagevent", lazy=True, cascade="all, delete-orphan"
    )
    userid = db.relationship(
        "User", backref="tagevent", lazy=True, cascade="all, delete-orphan"
    )
    comments =  db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.DateTime, nullable=False)
    weight =  db.Column(db.Integer, nullable=False)
    length =  db.Column(db.Integer, nullable=False)
    lat =  db.Column(db.Float, nullable=False)
    lon =  db.Column(db.Float, nullable=False)