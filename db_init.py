__author__ = 'tom'
#coding=utf-8

from app.models import User,Role,Sex, Productstatus
from app import db

status = Productstatus()
status.status = 1
status.statusname = u'启用'
db.session.add(status)
db.session.commit()

status = Productstatus()
status.status = 0
status.statusname = u'禁用'
db.session.add(status)
db.session.commit()

role = Role()
role.id = 1
role.role = u'管理员'
role.roletype = 1
db.session.add(role)
db.session.commit()

role = Role()
role.id = 2
role.role = u'会员'
role.roletype = 2
db.session.add(role)
db.session.commit()

man = Sex()
man.sex = 1
man.sexname = u'男'
db.session.add(man)
db.session.commit()

woman = Sex()
woman.sex = 0
woman.sexname = u'女'
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