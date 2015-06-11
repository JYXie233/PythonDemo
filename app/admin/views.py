__author__ = 'tom'
from flask import Blueprint,render_template,g,redirect,url_for
from flask.ext.login import login_required
from app.models import User
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
def index():
    if not g.user.isadmin:
        return redirect(url_for('users.login'))
    user = g.user
    return render_template('admin/index.html', username = user.nickname)
