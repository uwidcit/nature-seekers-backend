from App.models import TurtleTag, Tag, Turtle
from App.database import db

import json

#----------Create turtleTag object
def create_turtleTag(
                    turtle_id,
                    tag_id,
                    location
                    ):
    tag = Tag.query.get(tag_id)
    turtle = Turtle.query.get(turtle_id)
    if tag and turtle:
        turtleTag = TurtleTag()
        turtleTag.turtle_id = turtle.id
        tag.turtle_id = turtle.id
        turtleTag.tag_id = tag.id
        turtleTag.location = location
        turtleTag.status = "ACTIVE"
        db.session.add(turtleTag)
        db.session.add(tag)
        db.session.commit()
        return turtleTag

def get_turtle_tag_by_id(tag_id):
    return TurtleTag.query.get(tag_id)
    
def get_turtle_tag_by_turtle_and_tag(tag_id, turtle_id):
    return TurtleTag.query.filter_by(turtle_id=int(turtle_id), tag_id=int(tag_id)).first()

#----------Get turtleTag by turtleTag_id
def get_turtleTag(turtleTag_id):
    return TurtleTag.query.get(turtleTag_id)

#----------Get turtle tag by turtle_id
def get_turtleTag_by_turtle(turtle_id):
    turtleTags = TurtleTag.query.filter_by(turtle_id=turtle_id).all()
    return [turtleTag.toJSON() for turtleTag in turtleTags]

#----------Get all turtleTags
def get_all_turtleTag_json():
    allTurtles = Turtle.query.all()
    return [
        {
            "turtle": turtle.toJSON(),
            "tags": [tag.toJSON() for tag in turtle.tags]
        } for turtle in allTurtles
    ]
    
#----------Delete an turtleTag by excavation_id
def delete_turtleTag(turtleTag_id):
    turtleTag = get_turtleTag(turtleTag_id)
    if turtleTag:
        db.session.delete(turtleTag)
        return db.session.commit()
    return None

#----------Update organization event name 
def edit_turtleTag(turtle_tag_id, turtle_id, location, status):
    turtleTag = TurtleTag.query.filter_by(id=turtle_tag_id).first()
    if turtleTag:
        turtleTag.status = status
        turtleTag.turtle_id = turtle_id
        turtleTag.location = location
        db.session.add(turtleTag)
        db.session.commit()
        return turtleTag