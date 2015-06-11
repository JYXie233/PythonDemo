__author__ = 'tom'
# -*- coding: utf8 -*-
from wtforms.validators import ValidationError
from flask import session

class RandCode(object):
    def __init__(self, message=None):

        if not message:
            message=u'验证码错误'
        self.message = message

    def __call__(self, form, field):
        if 'rand_code' in session:
            randcode = session['rand_code']
            print randcode,field.data
            if randcode != field.data:
                print 'yanzhenmacuowu'
                raise ValidationError(self.message)

class Unique(object):
    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class Length(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'长度必须在%i 和 %i 之间.' % (min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)