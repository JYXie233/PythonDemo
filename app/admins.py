__author__ = 'Tom'
# coding=gbk
from flask import request,session

from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.wtf import Form
from app import app,db,babel,admin,lm
from models import User
from flask.ext import login

class MyView(ModelView):
    column_labels = dict(nickName=u'用户名', realName=u'真实姓名')
    def is_accessible(self):
        return login.current_user.is_authenticated()


