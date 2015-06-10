__author__ = 'tom'
# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.utils.validators import Unique,Length
from app.models import User

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    LANGUAGES = ['zh']
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