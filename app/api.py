__author__ = 'Tom'
from app import app
path = 'api'
@app.route('/' + path + '/<user>')
def api(user):
    print(user)
    return "hello api"