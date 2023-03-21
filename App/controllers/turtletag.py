from App.models import TurtleTag, TagEvent
from App.database import db

def create_turtle_tag (tageventid, code, status, location):
    new_turtletag = TurtleTag (tageventid=tageventid, code=code, status=status, location=location)

    db.session.add(new_turtletag)
    db.session.commit()

    return new_turtletag


def get_turtle_tag (turtletagid):
    return TurtleTag.query.get(turtletagid)

def get_all_turtle_tags():
    return TurtleTag.query.all()


def update_turtleTag (turtletagid, status=None, location=None):
    turtle_tag = get_turtle_tag(turtletagid)

    if turtle_tag:

        if status:
            TurtleTag.status = status

        if location:
            TurtleTag.location = location

        db.session.add(turtle_tag)
        db.session.commit()

        return turtle_tag

    return None

def get_all_turtletags_json():
    turtletags = TurtleTag.query.all()
    if not turtletags:
        return []
    return [turtletag.toJSON() for turtletag in turtletags]


def delete_turtle_tag(id):
    tag = get_turtle_tag(id)
    if tag:
        db.session.delete(tag)
        return db.session.commit()
    return None

def get_turtle_tag_by_turtleId(turtleId):
    tagEvents = TagEvent.query.filter_by(turtleid=turtleId).all()
    if not tagEvents:
        return ["No Tag Events"]
    
    turtle_tags = []
    for tagEvent in tagEvents:
        tag = TagEvent.query.get(tagEvent.tageventid)
        turtle_tags += [tag]

    if not turtle_tags:
        return["No  Turtle Tags"]
    
    return [turtle_tag.toJSON() for turtle_tag in turtle_tags]