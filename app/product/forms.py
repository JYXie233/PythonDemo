__author__ = 'tom'
#coding=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required,Optional

class AddForm(Form):
    title = StringField(u'标题', validators=[DataRequired()])
    description = StringField(u'产品描述', validators=[DataRequired()])
    price = StringField(u'产品价格', validators=[DataRequired()])
    vipprice = StringField(u'产品会员价格', validators=[Optional()])
    shopkeeper = StringField(u'商家', validators=[DataRequired()])
    yieldly = StringField(u'产地', validators=[DataRequired()])
    sellcount = StringField(u'销售量', validators=[DataRequired()])
    image = StringField(u'图片URL', validators=[DataRequired()])
    url = StringField(u'产品URL', validators=[DataRequired()])