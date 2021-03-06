__author__ = 'tom'
#coding=utf-8
from flask import flash,Blueprint,redirect,render_template,request,url_for,session,g,jsonify
from flask.ext.login import login_user, login_required, logout_user,current_user
from .forms import LoginForm, RegisterForm, EditForm
from app.models import User,Role
from app import db,bcrypt,app,checkAdmin
from app.utils.ImageUtils import create_validate_code
import StringIO,datetime

################
#### config ####
################
users_bp = Blueprint(
    'users',__name__,
    template_folder='templates',
    static_folder='static'
)

################
#### routes ####
################
@users_bp.route('/')
@users_bp.route('/index')
@login_required
@checkAdmin
def index():
    # users = User.query.filter_by(role_id=Role.query.filter_by(roletype=1).first().roletype)
    users = User.query.join(User.role).filter(Role.roletype==1)
    return render_template('users/index.html',users = users)

@users_bp.route('/member')
@login_required
@checkAdmin
def member():
    # users = User.query.filter_by(role_id=Role.query.filter_by(roletype=1).first().roletype)
    users = User.query.join(User.role).filter(Role.roletype==2)
    return render_template('users/index.html',users = users)

@users_bp.route('/del/<userid>')
@login_required
@checkAdmin
def delete(userid):
    users = User.query.filter_by(id=userid).first()
    db.session.delete(users)
    db.session.commit()
    return redirect(url_for('.index'))

@users_bp.route('/edit/<userid>', methods=['GET'])
@users_bp.route('/edit/<userid>',methods=['POST'])
@login_required
@checkAdmin
def edit(userid):
    if not g.user.isadmin:
        return redirect(url_for('users.login'))
    user = User.query.filter_by(id=userid).first()
    form = EditForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print 'validate'
            form.populate_obj(user)
            db.session.commit()
            flash(u'保存成功')
            return redirect(url_for('users.index'))

    form.sex.data=user.sex
    form.role.data=user.role
    return render_template('/users/edit.html',user = user, form = form)


@users_bp.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(nickname=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                user.lastlogindate = datetime.datetime.now()
                db.session.commit()
                login_user(user)
                if user.isadmin:
                    return redirect(url_for('admin.index'))
                else:
                    return redirect(url_for('home.index'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@users_bp.route('/logout')   # pragma: no cover
@login_required   # pragma: no cover
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.index'))


@users_bp.route('/add/', methods=['GET', 'POST'])   # pragma: no cover
@checkAdmin
def add():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                name=form.nickname.data,
                email=form.email.data,
                password=form.password.data,
                isadmin= True
            )
            user.role_id = form.role.data.id
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users.index'))
    return render_template('users/add.html', form=form)

@users_bp.route('/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.nickname.data,
            email=form.email.data,
            password=form.password.data,
            isadmin= True
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)

@users_bp.route('/randCode/<num>')
def randCode(num):
    image, code = create_validate_code()
    buf = StringIO.StringIO()
    image.save(buf,'JPEG',quality=70)
    session['rand_code'] = code
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

@app.before_request
def before_request():
    g.user = current_user