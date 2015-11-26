__author__ = 'miyatake_y'

import bottle
from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=1046, debug=True, reloader=True)