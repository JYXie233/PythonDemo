__author__ = 'tom'
from flask import Blueprint,render_template,g,redirect,url_for
from flask.ext.login import login_required
from app.models import User
from app import checkAdmin
################
#### config ####
################
admin_bp = Blueprint(
    'admin',__name__,
    static_folder='static',
    template_folder='templates'
)

@admin_bp.route('/')
@admin_bp.route('/index')
@login_required
@checkAdmin
def index():
    user = g.user
    return render_template('admin/index.html', username = user.nickname)
