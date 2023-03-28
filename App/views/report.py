from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime
#from App.models import Turtle

from App.controllers import (
    longest_turtle,
    get_turtle
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
        case 6: #largest by length
            turtleBio = longest_turtle(from_date, to_date)
            turtle = get_turtle(turtleBio.turtle_id)

            return [turtle.toJSON()] + [turtleBio.toJSON()]
#    report = create_report(name=data["name"], sex=data["sex"], dob=dob, species=data["species"])
#
#    if report:
#        return jsonify(report.toJSON()), 201
#
    return jsonify({"error": "report not created"}), 400
