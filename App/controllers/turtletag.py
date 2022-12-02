from App.models import TurtleTag
from App.database import db

def create_turtle_tag (tageventid, code, status, location):
    new_turtletag = TurtleTag (tageventid=tageventid, code=code, status=status, location=location)

    db.session.add(new_turtletag)
    db.session.commit()

    return new_turtletag


def get_turtle_tag (id):
    return TurtleTag.query.get(id)


def update_turtleTag (id, status=None, location=None):
    turtle_tag = get_turtle_tag(id)

    if turtle_tag:

        if status:
            TurtleTag.status = status

        if location:
            TurtleTag.location = location

        db.session.add(turtle_tag)
        db.session.commit()

        return turtle_tag

    return None

# return all turtletags in json format
def get_turtles_json():
    turtletags = TurtleTag.query.all()
    if not turtletags:
        return []
    return [turtletag.toJSON() for turtletag in turtletags]
