from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime
#from App.models import Turtle

from App.controllers import (

    new_turtleTags,
    longest_turtle,
    shortest_turtle,
    heaviest_turtle,
    lightest_turtle,
    get_turtle,
    population_trend
)

report_views = Blueprint('report_views', __name__, template_folder='../templates')

@report_views.route('/api/report/<int:report_id>/<from_date>/<to_date>', methods=['GET'])
###@jwt_required()
def get_report(report_id, from_date, to_date):

    #get from_date as python date object
    date_components = from_date.split('-')
    year, month, day = [int(item) for item in date_components]
    from_date = date(year, month, day)

    #get data as python date object
    date_components = to_date.split('-')
    year, month, day = [int(item) for item in date_components]
    to_date = date(year, month, day)

    match report_id:
        
        case 1: #-------Population Trends with Time
            date_list, pop_list = population_trend(from_date, to_date)
            return [date_list, pop_list]

        case 4: #new tags
            turtleTags = new_turtleTags(from_date, to_date)
            return [turtleTag.toJSON() for turtleTag in turtleTags]

        case 6: #largest by length
            turtleBio = longest_turtle(from_date, to_date)
            turtle = get_turtle(turtleBio.turtle_id)
            return [turtle.toJSON()] + [turtleBio.toJSON()]
        
        case 7: #smallest by length
            turtleBio = shortest_turtle(from_date, to_date)
            turtle = get_turtle(turtleBio.turtle_id)
            return [turtle.toJSON()] + [turtleBio.toJSON()]

        case 8: #largest by weight
            turtleBio = heaviest_turtle(from_date, to_date)
            turtle = get_turtle(turtleBio.turtle_id)
            return [turtle.toJSON()] + [turtleBio.toJSON()]
        
        case 9: #smallest by weight
            turtleBio = lightest_turtle(from_date, to_date)
            turtle = get_turtle(turtleBio.turtle_id)
            return [turtle.toJSON()] + [turtleBio.toJSON()]
    return jsonify({"error": "Report not created"}), 400
