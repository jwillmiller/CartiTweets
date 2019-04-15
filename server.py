# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:25:54 2019

@author: willm

Load sqlite database content onto localhost webpage
http://127.0.0.0:5000 to see content
"""

from flask import Flask, render_template
import sqlite3

db = "../twit_data.db" # database


app = Flask(__name__)


def get_links():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # read from database
    c.execute("SELECT * from uzi_links  ORDER BY datetime")
    result = c.fetchall()
    links = []
    
    for tweet in result:
        links.append(tweet['link'])
        
    conn.close()

    return links
    

@app.route('/carti')
def listLinks():
    links = get_links()
    return render_template('links.html', links=links)

if __name__ == '__main__':
    app.run()