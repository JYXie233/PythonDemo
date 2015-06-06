__author__ = 'Tom'
import os
from flask.ext.login import LoginManager
from config import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

from .models import User,Post

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app.views import views
from .admin import admin

app.register_blueprint(views,url_prefix='/')
app.register_blueprint(admin,url_prefix='/admin')
