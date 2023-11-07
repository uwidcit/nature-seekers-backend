from App.models import Tag
from App.database import db

import json

#----------Create Tag object
def create_tag(code):
    
    newTag = Tag(code=code)
    
    db.session.add(newTag)
    db.session.commit()
    return newTag

#----------Get Tag by Tag_id
def get_tag(id):
    return Tag.query.get(id)

# #----------Get turtle tag by turtle_id
# def get_Tag_by_turtle(turtle_id):
#     Tags = Tag.query.filter_by(turtle_id=turtle_id).all()
#     return [Tag.toJSON() for Tag in Tags]

#----------Get all Tags
def get_all_tags_json():
    Tags = Tag.query.all()
    if not Tags:
        return []
    return [Tag.toJSON() for Tag in Tags]
    
#----------Delete an Tag by excavation_id
def delete_tag(id):
    Tag = get_tag(id)
    if Tag:
        db.session.delete(Tag)
        return db.session.commit()
    return None

#----------Update organization event name 
def edit_tag(id, code):
    tag = Tag.query.filter_by(id=id).first()
    if tag:
        tag.code = code
        db.session.add(tag)
        db.session.commit()
        return tag