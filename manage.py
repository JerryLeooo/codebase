# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('.'))

from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import MigrateCommand

from main import app as web

app = web.create_app()
manager = Manager(app)

def _make_context():
    from main.core import db
    from main import models

    return dict(app=app, db=db, models=models)

@manager.command
def test():
    import subprocess
    code = subprocess.call(['py.text', 'tests', '--cov', 'main', '--verbose'])
    return code

manager.add_command('server', Server(host='0.0.0.0', use_reloader=True))
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))
