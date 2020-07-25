from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_openid import OpenID
from config import Config, basedir

import os


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import routes, models, admin
