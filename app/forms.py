__author__ = 'Tom'
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    passwd = PasswordField('passwd',validators=[DataRequired()])
    remember_me = BooleanField('remomeber_me', default=True)