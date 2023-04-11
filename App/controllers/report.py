from datetime import date, timedelta

from flask import jsonify, render_template_string
from App.models import TurtleBio, Turtle, TurtleEvent, Nest
from App.database import db

import json


def population_for_given_date(on_date):
    pop = 0
    turtles = Turtle.query.filter(Turtle.dob <= on_date)
    for turtle in turtles:
        pop += 1
    # pop = len(turtles)
    return pop

# ----------Report 1 - population trend with time
def population_trend(from_date, to_date):

    delta = to_date - from_date
    date_list = [(from_date + timedelta(days=i)).strftime('%Y-%m-%d')
                 for i in range(delta.days+1)]

    turtle_pop = []
    for given_date in date_list:

        turtle_pop += [population_for_given_date(given_date)]

    chart_data = {

        'type': 'Line',
        'data': {
            'labels': date_list,
            'datasets': [
                {
                    'label': 'Population',
                    'data': turtle_pop,
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 1,

                }
            ]
        },
        'options': {
            'responsive': True,
            'maintainAspectRatio': True,
            # 'scales': {
            #     'y': {
            #         'beginAtZero': True
            #     }
            # }
        }


    }

    return jsonify(chart_data)

#----------Report 2 - Nest Distribution by Zones
def nest_distributions(from_date, to_date):
    nests = Nest.query.filter(Nest.timestamp.between(from_date, to_date))

    zone_1 = 0
    zone_2 = 0
    zone_3 = 0
    zone_4 = 0
    zone_5 = 0
    zone_6 = 0
    zone_7 = 0
    zone_8 = 0
    zone_9 = 0
    zone_10 = 0
    zone_11 = 0
    zone_12 = 0
    zone_13 = 0

    for nest in nests:
        match nest.zone:

            # --if  nest in zone 1
            case 1: zone_1 += 1
            case 2: zone_2 += 1
            case 3: zone_3 += 1
            case 4: zone_4 += 1
            case 5: zone_5 += 1
            case 6: zone_6 += 1
            case 7: zone_7 += 1
            case 8: zone_8 += 1
            case 9: zone_9 += 1
            case 10: zone_10 += 1
            case 11: zone_11 += 1
            case 12: zone_12 += 1
            case 13: zone_13 += 1

    zone_list = [zone_1, zone_2, zone_3, zone_4, zone_5, zone_6,
                 zone_7, zone_8, zone_9, zone_10, zone_11, zone_12, zone_13]

    chart_data = {

        'type': "Pie",
        'data': {
            'labels': ['zone_1', 'zone_2', 'zone_3', 'zone_4', 'zone_5', 'zone_6', 'zone_7', 'zone_8', 'zone_9', 'zone_10', 'zone_11', 'zone_12', 'zone_13'],
            'datasets': [{
                'backgroundColor': [
                    "#b91d47",
                    "#00aba9",
                    "#2b5797",
                    "#e8c3b9",
                    "#1e7145",
                    "#A23E48",
                    "#D13D40",
                    "#FF3C38",
                    "#FF643D",
                    "#FF8C42",
                    "#6699CC",
                    "#8DB0B7",
                    "#FFF275"


                ],
                'data': zone_list
            }]
        },
        'options': {
            'title': {
                'display': True,
                'text': "Nest Distribution by Zones",                
            },
            'width': 200, 
            'height': 200 
        }

        # 'type': "Bar",
        # 'data': {
        #     'labels': ['zone_1', 'zone_2', 'zone_3', 'zone_4', 'zone_5', 'zone_6', 'zone_7', 'zone_8', 'zone_9', 'zone_10', 'zone_11', 'zone_12', 'zone_13'],
        #     'datasets': [{
        #         'backgroundColor': 'rgba(0,0,255,1.0)',
        #         'data': zone_list
        #     }]
        # },
        # 'options': {
        #     'responsive': True,
        #     'maintainAspectRatio': True,
        # }
    }

    return jsonify(chart_data)

#----------Report 3 - New turtles between from_date to to_date
def new_turtles(from_date, to_date):
    turtles = Turtle.query.filter(Turtle.dob.between(from_date, to_date))

    turtles_list = []
    for turtle in turtles:
        turtles_list += [turtle.toJSON()]

    data = {
        'title': 'New Turtles',
        'data': turtles_list,
        'type': "Turtle"

    }
    return jsonify(data)

#----------Report 4 - New turtle tags between from_date to to_date
def new_turtleTags(from_date, to_date):

    turtles = TurtleEvent.query.filter(TurtleEvent.timestamp.between(
        from_date, to_date), TurtleEvent.event_type == "TAG")

    turtles_list = []
    for turtle in turtles:
        turtles_list += [turtle.toJSON()]

    data = {
        'title': 'New Turtle Tags',
        'data': turtles_list,
        'type': "Tags"

    }
    return jsonify(data)



#---------- Report 6 - get largest turtle between from_date to to_date
def longest_turtle(from_date, to_date):

    largest_turtle_length = 0

    turtles = TurtleBio.query.filter(
        TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.length > largest_turtle_length):
            largest_turtle_length = turtle.length
            longest_turtle = turtle

    
    return longest_turtle

#---------- Report 7 - get smallest turtle between from_date to to_date
def shortest_turtle(from_date, to_date):

    shortest_turtle_length = 9999

    turtles = TurtleBio.query.filter(
        TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.length < shortest_turtle_length):
            shortest_turtle_length = turtle.length
            shortest_turtle = turtle
    return shortest_turtle

# Report 8 - get heaviest turtle between from_date to to_date


def heaviest_turtle(from_date, to_date):

    heaviest_turtle_weight = 0

    turtles = TurtleBio.query.filter(
        TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.weight > heaviest_turtle_weight):
            heaviest_turtle_weight = turtle.weight
            heaviest_turtle = turtle
    return heaviest_turtle

# Report 9 - get smallest turtle between from_date to to_date


def lightest_turtle(from_date, to_date):

    lightest_turtle_weight = 9999

    turtles = TurtleBio.query.filter(
        TurtleBio.timestamp.between(from_date, to_date))

    for turtle in turtles:
        if (turtle.weight < lightest_turtle_weight):
            lightest_turtle_weight = turtle.weight
            lightest_turtle = turtle
    return lightest_turtle
