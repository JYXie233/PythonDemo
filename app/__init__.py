__author__ = 'Tom'
# coding=gbk

from flask import Flask,redirect,url_for,abort,render_template
from flask.ext.login import LoginManager,current_user
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from functools import wraps

def checkAdmin(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        from flask import g
        if g.user.role.roletype == 1:
            return func(*args, **kwargs)
        abort(404)
    return decorated_view

app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


from .home.views import home_bp
app.register_blueprint(home_bp, url_prefix='/')


from .admin.views import admin_bp
from .users.views import users_bp
from .article.views import article_bp
from .product.views import product_bp

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(article_bp, url_prefix='/article')
app.register_blueprint(product_bp, url_prefix='/product')


from models import User

login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
