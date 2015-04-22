# coding=gbk
__author__ = 'Tom'
from flask import redirect,render_template,session,g,url_for,flash,request
from app import app
from forms import LoginForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import User

@app.route('/login', methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        session['remember_me'] = form.remember_me.data
        username = form.username.data
        userpassword = form.passwd.data
        print(username,userpassword)
        user = User.query.filter_by(nickname=username, password=userpassword).first()
        if user != None:
            login_user(user)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("index"))
        else:
            flash(u'没有这个用户')
    return render_template("login.html", form=form)


