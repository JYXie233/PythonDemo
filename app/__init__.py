__author__ = 'Tom'
# coding=gbk

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

from .admin.views import admin_bp
from .users.views import users_bp

app.register_blueprint(admin_bp)
app.register_blueprint(users_bp)

from models import User

login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))