__author__ = 'Tom'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'this-is-a-secret-key'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'http://<username>.openid.org.cn'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:5764050@localhost:3306/db_my?charset=utf8mb4'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

