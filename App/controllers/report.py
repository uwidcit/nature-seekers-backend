from App.models import TurtleBio 
from App.database import db

import json

#Report 7 - get largest turtle between from_date to to_date
def longest_turtle(from_date, to_date):
#   
    largest_turtle_length=0
    #longest_turtle = None

    turtles = TurtleBio.query.filter(TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.length > largest_turtle_length):
            largest_turtle_length = turtle.length
            longest_turtle = turtle
    return longest_turtle
#