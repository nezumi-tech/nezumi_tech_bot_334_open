#!/usr/bin/env python
# coding: utf-8

from twython import Twython

#twitterの認証情報
CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#ツイート
api.update_status(status = '334')
