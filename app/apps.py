from flask import Flask, Blueprint
from flask_restful import Api

from instance.config import app_config


version_1_blueprint = Blueprint('api', __name__)
api = Api(version_1_blueprint)

# The create_app function wraps the creation of a new Flask object, and returns it after it's loaded up with configuration settings
def create_app(config_name):
    app =Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False

    from .api.v1 import version1 as v1

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)
    


    return app
