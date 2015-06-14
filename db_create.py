__author__ = 'Tom'
#!flask/bin/python
#coding=utf-8

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
from app.models import User,Role,Sex

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
role = Role()
role.id = 1
role.role = u'admin'
role.roletype = 1
db.session.add(role)
db.session.commit()

role = Role()
role.id = 2
role.role = u'User'
role.roletype = 2
db.session.add(role)
db.session.commit()

man = Sex()
man.sex = 1
man.sexname = u'boy'
db.session.add(man)
db.session.commit()

woman = Sex()
woman.sex = 0
woman.sexname = u'girl'
db.session.add(woman)
db.session.commit()

user = User(
                name='tom',
                email='admin@admin.com',
                password='123456',
                isadmin= True
            )
user.role_id = 1
db.session.add(user)
db.session.commit()