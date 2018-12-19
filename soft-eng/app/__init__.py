from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

admin = Admin(app,template_mode='bootstrap3')
migrate = Migrate(app, db)

app.config.from_object(Config)

from app import routes, models
