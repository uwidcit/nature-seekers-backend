from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime

from flask_login import fresh_login_required, login_required

from App.views.user import admin_required

from App.controllers import (
    get_weight,
)

ar_views = Blueprint('ar_views', __name__, template_folder='../templates')


@ar_views.route('/api/ar', methods=['POST'])
def ar_action():

    width = request.json['width']
    length = request.json['length']

    weight_array = get_weight(length, width)

    weight = weight_array.tolist()

    return jsonify(weight)
   

