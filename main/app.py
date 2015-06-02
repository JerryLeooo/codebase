# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string

from main.settings import Config

blueprints = []

def create_app(register_bp=True):
    app = app = Flask(__name__)
    app.config.from_object(Config)
    if register_bp:
        register_blueprints(app)
    return app

def register_blueprints(app):
    for bp in blueprints:
        app.register_blueprint(import_string(bp))
