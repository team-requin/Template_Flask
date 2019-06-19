from flask import Flask
from mongoengine import *

def create_app(*config_cls):
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    # This setting for DB
    # connect(**flask_app.config['DB_SETTINGS'])

    return flask_app