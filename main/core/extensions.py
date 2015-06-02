# -*- coding: utf-8 -*-

from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
