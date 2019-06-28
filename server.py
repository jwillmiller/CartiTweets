# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:25:54 2019

@author: willm

Load sqlite database content onto localhost webpage
http://127.0.0.0:5000 to see content
"""

from flask import Flask, render_template
import sqlite3
#import tweepyStreamer as tw

db = "../twit_data.db" # database


app = Flask(__name__)


def get_links():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # read from database
    c.execute("SELECT * from carti_links  ORDER BY datetime")
    result = c.fetchall()
    links = []
    
    for tweet in result:
        links.append(tweet['link'])
        
    conn.close()

    return links

'''def getTwitter(num_tweets_to_grab):
    try:
        conn = sqlite3.connect(db)
        twit = tw.TwitterMain(num_tweets_to_grab, conn)
        twit.get_streaming_data()
        
    except Exception as e:
        print(e.__doc__)
        
    finally:
        conn.close()'''
    

@app.route('/carti', methods=['GET', 'POST'])
def listLinks():
    links = get_links()
    return render_template('links.html', links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)