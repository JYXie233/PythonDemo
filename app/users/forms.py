__author__ = 'tom'
# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required,Optional
from app.utils.validators import Unique,Length,RandCode
from app.models import User,Role,Sex

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    verify = StringField('verify',  validators=[DataRequired(), RandCode()])


def select_roles():
        choices = Role.query.all()
        return  [(c.id, c.role) for c in choices]

class RegisterForm(Form):
    nickname = StringField(
        u'用户名',
        validators=[DataRequired(), Length(min=3, max=25), Unique(
            User,
            User.nickname, message=u'该用户名已经存在')]
    )
    email = StringField(
        u'邮箱',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40), Unique(
            User,
            User.email, message=u'该邮箱已经存在')]
    )
    password = PasswordField(
        u'密码',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        u'重复密码',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )
    realname = StringField(
        u'真实姓名',
        validators=[Optional(), Length(min=2, max=25)]
    )
    role= QuerySelectField(
        u'用户角色',query_factory=lambda :Role.query.all(),get_pk=lambda x:x.id,get_label=lambda x:x.role
    )
    sex= QuerySelectField(
        u'性别',query_factory=lambda :Sex.query.all(),get_pk=lambda x:x.sex,get_label=lambda x:x.sexname
    )
    mobilenumber = StringField(u'手机号码')
    provinces = StringField(u'省份')
    city = StringField(u'城市')



class EditForm(Form):
    nickname = StringField(
        u'用户名',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    password = PasswordField(
        u'密码',
        validators=[Optional(), Length(min=3, max=25)]
    )
    realname = StringField(
        u'真实姓名',
        validators=[Optional(), Length(min=2, max=25)]
    )
    email = StringField(u'邮箱地址', validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    role= QuerySelectField(
        u'用户角色',validators=[Optional()],query_factory=lambda :Role.query.all(),get_pk=lambda x:x.id,get_label=lambda x:x.role
    )
    sex= QuerySelectField(
        u'性别',validators=[Optional()],query_factory=lambda :Sex.query.all(),get_pk=lambda x:x.sex,get_label=lambda x:x.sexname
    )
    mobilenumber = StringField(u'手机号码',validators=[Optional()])
    provinces = StringField(u'省份',validators=[Optional()])
    city = StringField(u'城市',validators=[Optional()])
