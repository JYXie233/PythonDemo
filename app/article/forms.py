__author__ = 'Tom'
#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField,TextField
from wtforms.validators import DataRequired
from app.utils.validators import Length

class ArticleForm(Form):
    title = StringField(
        u'文章标题',
        validators=[DataRequired(), Length(min=3, max=60)]
    )
    body = StringField(
        u'文章内容',
        validators=[DataRequired()]
    )