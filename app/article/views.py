__author__ = 'Tom'
#coding:utf-8
from flask import flash,Blueprint,redirect,render_template,request,url_for,session,g,json,make_response
from flask.ext.login import login_user, login_required, logout_user,current_user
from app.models import User,Post
from app import db,bcrypt,app
from app.utils.ImageUtils import create_validate_code
import StringIO,datetime
import os,re
from app.utils.uploader import Uploader

################
#### config ####
################
article_bp = Blueprint(
    'article',__name__,
    template_folder='templates',
    static_folder='static'
)


@article_bp.route('/')
@article_bp.route('/index')
@login_required
def index():
    if not g.user.isadmin:
        return redirect(url_for('users.login'))
    articles = Post.query.all()
    return render_template('article/index.html',articles = articles)

@login_required
@article_bp.route('/add')
def add():
    if not g.user.isadmin:
        return redirect(url_for('users.login'))
    articles = Post.query.all()
    return render_template('article/add.html',articles = articles)

@article_bp.route('/upload/', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    mimetype = 'application/json'
    result = {}
    action = request.args.get('action')


    with open(os.path.join(article_bp.static_folder, 'ueditor', 'php',
                           'config.json')) as fp:
        try:

            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}

    if action == 'config':

        result = CONFIG

    elif action in ('uploadimage', 'uploadfile', 'uploadvideo'):

        if action == 'uploadimage':
            fieldName = CONFIG.get('imageFieldName')
            config = {
                "pathFormat": CONFIG['imagePathFormat'],
                "maxSize": CONFIG['imageMaxSize'],
                "allowFiles": CONFIG['imageAllowFiles']
            }
        elif action == 'uploadvideo':
            fieldName = CONFIG.get('videoFieldName')
            config = {
                "pathFormat": CONFIG['videoPathFormat'],
                "maxSize": CONFIG['videoMaxSize'],
                "allowFiles": CONFIG['videoAllowFiles']
            }
        else:
            fieldName = CONFIG.get('fileFieldName')
            config = {
                "pathFormat": CONFIG['filePathFormat'],
                "maxSize": CONFIG['fileMaxSize'],
                "allowFiles": CONFIG['fileAllowFiles']
            }

        if fieldName in request.files:
            field = request.files[fieldName]
            uploader = Uploader(field, config, app.static_folder)
            result = uploader.getFileInfo()
        else:
            result['state'] = u'上传接口出错'

    elif action in ('uploadscrawl'):
        # 涂鸦上传
        fieldName = CONFIG.get('scrawlFieldName')
        config = {
            "pathFormat": CONFIG.get('scrawlPathFormat'),
            "maxSize": CONFIG.get('scrawlMaxSize'),
            "allowFiles": CONFIG.get('scrawlAllowFiles'),
            "oriName": "scrawl.png"
        }
        if fieldName in request.form:
            field = request.form[fieldName]
            uploader = Uploader(field, config, app.static_folder, 'base64')
            result = uploader.getFileInfo()
        else:
            result['state'] = u'上传接口出错'

    elif action in ('catchimage'):
        config = {
            "pathFormat": CONFIG['catcherPathFormat'],
            "maxSize": CONFIG['catcherMaxSize'],
            "allowFiles": CONFIG['catcherAllowFiles'],
            "oriName": "remote.png"
        }
        fieldName = CONFIG['catcherFieldName']

        if fieldName in request.form:

            source = []
        elif '%s[]' % fieldName in request.form:

            source = request.form.getlist('%s[]' % fieldName)

        _list = []
        for imgurl in source:
            uploader = Uploader(imgurl, config, app.static_folder, 'remote')
            info = uploader.getFileInfo()
            _list.append({
                'state': info['state'],
                'url': info['url'],
                'original': info['original'],
                'source': imgurl,
            })

        result['state'] = 'SUCCESS' if len(_list) > 0 else 'ERROR'
        result['list'] = _list

    else:
        result['state'] = u'请求地址出错'

    result = json.dumps(result)

    if 'callback' in request.args:
        callback = request.args.get('callback')
        if re.match(r'^[\w_]+$', callback):
            result = '%s(%s)' % (callback, result)
            mimetype = 'application/javascript'
        else:
            result = json.dumps({'state': u'callback参数不合法'})

    res = make_response(result)
    res.mimetype = mimetype
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return res