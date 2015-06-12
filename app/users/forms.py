__author__ = 'tom'
# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required,Optional
from app.utils.validators import Unique,Length,RandCode
from app.models import User

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    verify = StringField('verify',  validators=[DataRequired(), RandCode()])

class RegisterForm(Form):
    nickName = StringField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25), Unique(
            User,
            User.nickname, message=u'该用户名已经存在')]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40), Unique(
            User,
            User.email, message=u'该邮箱已经存在')]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )

class EditForm(Form):
    nickname = StringField(
        u'登录名',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    password = PasswordField(
        u'密码',
        validators=[Optional(), Length(min=3, max=25)]
    )
    realname = StringField(
        u'真实姓名',
        validators=[Optional(), Length(min=3, max=25)]
    )
    email = StringField(u'邮箱地址', validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
