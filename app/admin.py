__author__ = 'Tom'
from flask import render_template, flash, redirect, session, url_for, request, g,Blueprint

admin = Blueprint('admin',__name__)

@admin.route('/')
@admin.route('/index')
def index():
    return render_template('admin/index.html')