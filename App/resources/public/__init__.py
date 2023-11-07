"""Public Controller

The public module contains all the endpoints that are required to provide functionality to non-logged (public) in users

This would include functionality such as logging in, registering, resetting password or any other route that would NOT
require a user to be logged in to the application

"""

from flask import Blueprint
from flask_restful import Api


def get_public_blueprint() -> Blueprint:
    """This function is responsible for creating and setting up the public routes.

    Public routes would be accessible using the following URL layout:
        - http(s)://<host>:<port>/api/<endpoint>
    """

    from .register import PublicRegisterResource

    # The main blueprint for the public APIs.
    public_blueprint = Blueprint('public', __name__, url_prefix='')

    public_api = Api(public_blueprint)

    public_api.add_resource(PublicRegisterResource, '/register')

    return public_blueprint