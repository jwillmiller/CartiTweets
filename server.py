# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:25:54 2019

@author: willm

Basic server
"""

#from os import environ
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

"""
app.run(host = '0.0.0.0', environ.get('PORT'))
"""