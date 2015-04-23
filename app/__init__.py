__author__ = 'Tom'
import os
from flask.ext.login import LoginManager
from config import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .models import User,Post

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models, login