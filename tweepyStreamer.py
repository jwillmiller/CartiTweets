# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:43:27 2019

@author: willm

Twitter streamer
"""

import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import local_config as lc
import sqlite3

 
db = "../twit_data.db" # database

# tweepy Listener
class MyListener(StreamListener):
    
    def __init__(self, num_tweets_to_grab, stats):
        super(MyListener, self).__init__()
        self.counter = 0
        self.num_tweets_to_grab = num_tweets_to_grab
        self.stats = stats
        
    def on_status(self, status):
        try:
            if 'urls' in status.entities: #first check for links
                url_params = ['soundcloud', 'youtube']
                for item in status.entities['urls']:
                    if any(y in item['expanded_url'].lower() for y in url_params):
                        self.stats.add_link(item['expanded_url'])
                        self.counter += 1
                        print(self.counter) # visual tracking for progress
            
            #then check for tweet text
            search_params = ['youtu.be','youtube.com','soundcloud.com','soundcloud']
            if any(x in status.text.lower() for x in search_params):
                self.stats.add_link(status.text)
                self.counter += 1
                print(self.counter) # visual tracking for progress

            if self.counter == self.num_tweets_to_grab:
                return False
            
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
    
    
# main Twitter class    
class TwitterMain():
    def __init__(self, num_tweets_to_grab, conn):
        self.auth = tweepy.OAuthHandler(lc.consumer_key, lc.consumer_secret)
        self.auth.set_access_token(lc.access_token, lc.access_secret)
 
        self.api = tweepy.API(self.auth)
        self.num_tweets_to_grab = num_tweets_to_grab
        self.stats = stats()
        self.conn = conn
        self.c = self.conn.cursor()
        
    def get_streaming_data(self):
        twitter_stream = Stream(self.api.auth, MyListener(num_tweets_to_grab=self.num_tweets_to_grab, stats=self.stats ))
        twitter_stream.filter(track=['playboi carti','carti'])
        #twitter_stream.filter(track=['lil uzi vert'])
        
        links = self.stats.get_stats()
        
        for t in links:
            self.c.execute("INSERT INTO carti_links VALUES (?, DATETIME('now'))", (t,))
        
        self.conn.commit() # commit to database
        

# allows us to pass around list of links
class stats():
    def __init__(self):
        self.found_links = []
        
    def add_link(self, link):
        self.found_links.append(link)
        
    def get_stats(self):
        return self.found_links
    
            
if __name__ == "__main__":
    num_tweets_to_grab = 5
    try:
        conn = sqlite3.connect(db)
        twit = TwitterMain(num_tweets_to_grab, conn)
        twit.get_streaming_data()
        
    except Exception as e:
        print(e.__doc__)
        
    finally:
        conn.close()
    
    
    