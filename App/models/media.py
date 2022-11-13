from App.database import db

class Media(db.Model):
    pictureid = db.Column(db.Integer, primary_key=True)
    tageventid = db.relationship(
        "Tag", backref="tagevent", lazy=True, cascade="all, delete-orphan"
    )
    filename = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)