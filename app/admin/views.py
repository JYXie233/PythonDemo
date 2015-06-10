__author__ = 'tom'
from flask import Blueprint

################
#### config ####
################
admin_bp = Blueprint(
    'admin',__name__,
    template_folder='templates'
)
