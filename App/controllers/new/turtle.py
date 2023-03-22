from App.models import Turtle
from App.database import db

import json

#Create turtle object
def create_turtle(
                    name,
                    sex,
                    dob,
                    species):
    
    newturtle = Turtle(
                        name,
                        sex,
                        dob,
                        species
                    )
    
    db.session.add(newturtle)
    db.session.commit()
    return newturtle

#Get turtle by turtle_id
def get_turtle(turtle_id):
    return Turtle.query.get(turtle_id)

#Get all turtles
def get_all_turtle_json():
    turtles = Turtle.query.all()
    if not turtles:
        return []
    return [turtle.toJSON() for turtle in turtles]

#Update turtle data 
def edit_turtle_data(turtle_id, new_name, new_sex, new_dob, new_species):
    turtle = Turtle.query.filter_by(turtle_id=turtle_id).first()
    if not turtle:
        return ["Turtle not found"]

    turtle.name = new_name
    turtle.sex = new_sex
    turtle.dob = new_dob
    turtle.species = new_species

    db.session.add(turtle)
    db.session.commit()
    
#Delete an turtle by excavation_id
def delete_turtle(turtle_id):
    turtle = get_turtle(turtle_id)
    if turtle:
        db.session.delete(turtle)
        return db.session.commit()
    return None