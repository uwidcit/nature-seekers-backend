from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required

from datetime import date, datetime

from flask_login import fresh_login_required, login_required

from App.views.user import admin_required

from App.controllers import (
    create_tag,
    get_tag,
    get_all_tags_json,
    delete_tag,
    edit_tag
)

tag_views = Blueprint('tag_views', __name__, template_folder='../templates')

#-----------Create tag
@tag_views.route('/api/tags', methods=['POST'])
def create_tag_action():
    data = request.json

    #get data as python date objects
    tag = create_tag(code=data["code"])

    if tag:
        return jsonify(tag.toJSON()), 201

    return jsonify({"error": "tag not created"}), 400


#-------Get tag by Id
@tag_views.route('/api/tags/<int:tagid>', methods=['GET'])
def get_tag_action(tagid):
    tag = get_tag(tagid)

    if tag:
        return jsonify({
            "tag": tag.toJSON(),
            "details": tag.detail.toJSON() if tag.detail else {}
        }), 200

    return jsonify({"error": "tag not found"}), 404


#-------Get All tags
@tag_views.route('/api/tags', methods=['GET'])
def get_all_tag_action():
    #tags = []
    tags = get_all_tags_json()

    return jsonify(tags)


#-------Delete tag by Id
@tag_views.route('/api/tags/delete/<int:tagid>', methods=['DELETE'])
def delete_tag_action(tagid):
  
    tag = get_tag(tagid)

    if not tag:
        return jsonify(error="this is a custom error Bad ID or unauthorized"), 404

    delete_tag(tagid)
    return jsonify(message="tag deleted!"), 200


#-------Edit tag
@tag_views.route('/api/tags/edit/<int:tag_id>', methods=["PUT"])
#@admin_required
def edit_tag_action(tag_id):
    data = request.json

    tag = edit_tag(id=tag_id, code=data["code"],)
    if tag:
        return jsonify(tag.toJSON()), 201
    return jsonify(error="tag not edited"), 400