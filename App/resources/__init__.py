from flask import Blueprint, Flask

def register_api_v2(app: Flask):
    """ This function sets up the routes for v2.

    The endpoints on this application would fall under 4 categories
        - Admin APIs: These endpoints are in the form /admin/<endpoint> and would provide admin-only functionality
        - User APIs: These endpoints are in the form /user/<endpoint> and are used by mobile and web users
        - Common APIs: These endpoints are in the form /common/<endpoint> and are used by both admin and regular users.
            e.g. login, logout, forgot password etc.
        - Public APIs: These endpoints are in the form /endpoint and are used by users that are not logged in to the
        system.

    All APIs will be prefixed with /api. Therefore, the full endpoint for the application will be as follows
        - Admin APIs: http(s)://<host>:<port>/api/v2/admin/<endpoint>
        - User APIs: http(s)://<host>:<port>/api/v2/user/<endpoint>
        - Common APIs: http(s)://<host>:<port>/api/v2/common/<endpoint>
        - Public APIs: http(s)://<host>:<port>/api/v2/<endpoint>

    """
    api_bp = Blueprint('api', __name__, url_prefix='/api/v2')

    from .public import get_public_blueprint

    api_bp.register_blueprint(get_public_blueprint())
    app.register_blueprint(api_bp)