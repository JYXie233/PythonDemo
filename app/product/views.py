__author__ = 'tom'
#coding=utf-8
from flask import flash,Blueprint,redirect,render_template,request,url_for,session,g,jsonify
from flask.ext.login import login_user, login_required, logout_user,current_user
from app import checkAdmin,db
from app.models import Product
from .forms import AddForm
import datetime
################
#### config ####
################
product_bp = Blueprint(
    'product',__name__,
    template_folder='templates',
    static_folder='static'
)

################
#### routes ####
################

@product_bp.route('/')
@product_bp.route('/index')
@login_required
@checkAdmin
def index():
    products = Product.query.all()
    return render_template('product/index.html', products = products)

@product_bp.route('/add/', methods=['GET', 'POST'])   # pragma: no cover
@checkAdmin
def add():
    form = AddForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            product = Product()
            product.createdate = datetime.datetime.now()
            form.populate_obj(product)
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('product.index'))
    return render_template('product/add.html', form=form)