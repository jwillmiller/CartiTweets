# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:25:54 2019

@author: willm

Basic server
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = 'Will Miller'
    name = 'Will'
    return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

"""
app.run(host = '0.0.0.0', environ.get('PORT'))
"""