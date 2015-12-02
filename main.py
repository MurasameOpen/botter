# -*- encoding: utf-8 -*-
# coding: utf-8
# import os

__author__ = 'miyatake_y'

import bottle
import jinja2
import secret
import Twitter


from bottle import route, post, request, run
from bottle import TEMPLATE_PATH, jinja2_template as template

TEMPLATE_PATH.append("./template")

global twitter_
twitter_=None



def HomeHandler():
    global twitter_
    return template("home.j2", posts=twitter_.home_timeline())



# TODO: Method指定する
# とりあえずはログインは自動
@route('/')
def HomeHandler_():
    return HomeHandler()

@post('/1/twitter/post')
def UpdateHandler_():
    global twitter_
    msg = request.forms.decode().get('status')
    print("post:"+msg)
    res = twitter_.update(msg)
    return HomeHandler()



twitter_ = Twitter.Twitter(secret.consumer_key, secret.consumer_secret, secret.access_token, secret.access_token_secret)

if __name__ == "__main__":
    run(host='localhost', port=1046, debug=True, reloader=True)
    #    if os.environ.get('BOTTLE_CHILD'):
    print("child")


