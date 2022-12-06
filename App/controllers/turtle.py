from App.models import Turtle
from App.database import db

def create_turtle (name, sex, dob):
    new_turtle = Turtle (name=name, sex=sex, dob=dob)

    db.session.add(new_turtle)
    db.session.commit()

    return new_turtle


def get_turtle (turtleid):
    return Turtle.query.get(turtleid)

def get_all_turtles():
    return Turtle.query.all()


def update_turtle(turtleid, name=None, sex=None, dob=None):
    turtle1 = get_turtle(turtleid)

    if turtle1:

        if name:
            turtle1.name = name

        if sex:
            turtle1.sex = sex

        if dob:
            turtle1.dob = dob

        db.session.add(turtle1)
        db.session.commit()

        return turtle1

    return None


def get_all_turtles_json():
    turtles = get_all_turtles()

    if not turtles:
        return []

    return [turtle.toJSON() for turtle in turtles]
