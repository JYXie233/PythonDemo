__author__ = 'Tom'
from app import db,bcrypt
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True)
    realname = db.Column(db.String(64), index=True)
    mobilenumber = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    password = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    ipaddress = db.Column(db.String(64), index=True)
    provinces = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    isadmin = db.Column(db.Boolean)
    lastlogindate = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __init__(self, name, email, password, isadmin):
        self.nickname = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.isadmin = isadmin

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(140))
    create_date = db.Column(db.DateTime)
    edit_date = db.Column(db.DateTime)

    def __init__(self, title, user_id, create_date, body):
        self.body = body
        self.title = title
        self.create_date = create_date
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(20))
    roletype = db.Column(db.Integer)
    user_id=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % (self.role)
