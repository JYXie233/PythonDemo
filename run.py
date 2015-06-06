__author__ = 'Tom'
from app import app
if __name__ == '__main__':
    app.run('0.0.0.0',port=1234,debug=True)