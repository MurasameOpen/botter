__author__ = 'miyatake_y'

import bottle
import jinja2
from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template

TEMPLATE_PATH.append("./template")

@route('/hello/<name>')
def hello(name):
    return template('hello.j2', name=name)

run(host='localhost', port=1046, debug=True, reloader=True)