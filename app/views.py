from flask import render_template, flash, redirect, session, url_for, request, g,Blueprint
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import db, lm
from .forms import LoginForm
from .models import User,Post

views = Blueprint('views',__name__)

@views.route('/')
@views.route('/index')
def index():
    user = g.user
    posts = Post.query.order_by(Post.timestamp).limit(10).all()
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@views.route('/table')
def table():
    return render_template('tables.html')

@views.before_request
def before_request():
    g.user = current_user


@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@views.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author':user, 'body':'Test post #1'},
        {'author':user, 'body':'Test post #2'}
    ]
    return render_template('user.html', user = user, posts = posts)