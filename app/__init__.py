__author__ = 'Tom'
# coding=gbk
import os
from flask.ext.login import LoginManager
from config import basedir
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babelex import Babel

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
babel = Babel(app,default_locale='zh_CN')
admin = Admin(app,name=u'闰土后台管理')

from .models import User,Post

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app.views import views

app.register_blueprint(views,url_prefix='/')

from app.admins import MyView

admin.add_view(MyView(User, db.session,name=u'用户'))


@babel.localeselector
def get_locale():
    return 'zh_CN'