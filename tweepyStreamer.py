# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:43:27 2019

@author: willm

Twitter streamer
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from os import environ

#get API keys from Heroku environment
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_secret = environ['ACCESS_SECRET']
 
#Twitter OAuth
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
class MyListener(StreamListener):
    def on_status(self, status):
        try:
            with open('tweetData.txt', 'a') as f:
                data = '' #string of tweet data that will go to file
                #first check for links
                if 'urls' in status.entities:
                    url_params = ['soundcloud', 'youtube']
                    for item in status.entities['urls']:
                        if any(y in item['expanded_url'].lower() for y in url_params):
                            data += item['expanded_url']
                            print(item['expanded_url'])
                #then check for tweet text
                search_params = ['youtu.be','youtube.com','soundcloud.com','soundcloud']
                if any(x in status.text.lower() for x in search_params):
                    data = data + ', ' + status.text
                    print(status.text) 
                f.write(data) #write to file
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['playboi carti','carti'])
