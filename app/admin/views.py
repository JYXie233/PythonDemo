__author__ = 'tom'
from flask import Blueprint
from flask.ext.login import login_required
################
#### config ####
################
admin_bp = Blueprint(
    'admin',__name__,
    template_folder='templates',
    static_folder='static'
)

@admin_bp.route('/')
@admin_bp.route('/index')
@login_required
def index():

