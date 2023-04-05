from datetime import timedelta
from App.models import TurtleBio, Turtle, TurtleEvent
from App.database import db

import json

def population_for_given_date(on_date):
    pop=0
    turtles = Turtle.query.filter(Turtle.dob <= on_date)
    for turtle in turtles:
        pop += 1
    #pop = len(turtles)
    return pop

#Report 1 - population trend with time
def population_trend(from_date, to_date):

    delta = to_date - from_date
    date_list = [from_date + timedelta(days=i) for i in range(delta.days+1)]

    turtle_pop = []
    for given_date in date_list:
        turtle_pop += [population_for_given_date(given_date)]

    return date_list, turtle_pop

#Report 4 - get new turtle tags between from_date to to_date
def new_turtleTags(from_date, to_date): 

    turtles = TurtleEvent.query.filter(TurtleEvent.timestamp.between(from_date, to_date), TurtleEvent.event_type == "TAG")

    return turtles

#Report 6 - get largest turtle between from_date to to_date
def longest_turtle(from_date, to_date):

    largest_turtle_length=0

    turtles = TurtleBio.query.filter(TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.length > largest_turtle_length):
            largest_turtle_length = turtle.length
            longest_turtle = turtle
    return longest_turtle

#Report 7 - get smallest turtle between from_date to to_date
def shortest_turtle(from_date, to_date):
    
    shortest_turtle_length=9999

    turtles = TurtleBio.query.filter(TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.length < shortest_turtle_length):
            shortest_turtle_length = turtle.length
            shortest_turtle = turtle
    return shortest_turtle

#Report 8 - get heaviest turtle between from_date to to_date
def heaviest_turtle(from_date, to_date):

    heaviest_turtle_weight=0

    turtles = TurtleBio.query.filter(TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.weight > heaviest_turtle_weight):
            heaviest_turtle_weight = turtle.weight
            heaviest_turtle = turtle
    return heaviest_turtle

#Report 9 - get smallest turtle between from_date to to_date
def lightest_turtle(from_date, to_date):
    
    lightest_turtle_weight=9999

    turtles = TurtleBio.query.filter(TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.weight < lightest_turtle_weight):
            lightest_turtle_weight = turtle.weight
            lightest_turtle = turtle
    return lightest_turtle