# -*- encoding: utf-8 -*-
import tweepy



__author__ = 'miyatake_y'

base_url = "https://api.twitter.com/1.1/"
update_url="statuses/update.json"



class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key_ = consumer_key
        self.consumer_secret_ = consumer_secret
        self.auth_ = tweepy.OAuthHandler(consumer_key,consumer_secret)
        self.access_token_ = access_token
        self.access_token_secret_ = access_token_secret
        self.auth_.set_access_token(access_token,access_token_secret)
        self.twitter_ = tweepy.API(self.auth_)

    def update(self, msg):
        print("Twitter.update:" + msg)
        return(self.twitter_.update_status(status=msg))

    def home_timeline(self):
        return(self.twitter_.home_timeline())

    def test(self):
        return(self.twitter_.home_timeline()[0].text)
