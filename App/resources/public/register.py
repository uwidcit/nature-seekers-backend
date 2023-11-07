from flask_restful import Resource, request
from flask import jsonify, make_response
from App.models import User
from App.database import db


class PublicRegisterResource(Resource):
    def post(self):
        """This function is called when a POST request is made to /register as a public user.

        It would return a JSON object with a message that should be displayed to the user as follows:

        Result on Successful registration (HTTP Status 201 - Created):
            {
                "message": "Your account has been created successfully. Please proceed to log in to the application"
            }

        Result on Unsuccessful registration (HTTP Status 409 - Conflict) - due to user existing already:

            {
                "error": "It seems like you already have an account in the system. Please log in"
            }

        Result on unsuccessful registration (HTTP Status 400) - any other error
            {
                "error": "There was an error with creating your account. Please try again later"
            }

        """

        # TODO: Sanity check to make sure i'm getting all parameters. Make sure all keys are in the dictionary before
        #  proceeding

        json_data = request.get_json(force=True)
        first_name = json_data['firstname']
        last_name = json_data['lastname']
        email = json_data['email']
        password = json_data['password']

        user = User.query.filter_by(email=email).one_or_none()

        if user:
            return make_response(jsonify(error="It seems like you already have an account in the system. Please log in"), 409)

        user = User(firstname=first_name, lastname=last_name, email=email, password=password, username=email)

        try:
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify(message="Your account has been created successfully. Please proceed to log "
                                                 "in to the application"), 201)
        except Exception as e:
            db.session.rollback()

        return make_response(jsonify(message="There was an error with creating your account. Please try again later"),
                             400)