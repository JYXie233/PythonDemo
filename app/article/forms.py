__author__ = 'Tom'
from flask.ext.wtf import Form
from wtforms import StringField,BooleanField,PasswordField
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