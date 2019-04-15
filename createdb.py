# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:07:23 2019

@author: willm

create database using sqlite
"""

import sqlite3

db = "../twit_data.db"

conn = sqlite3.connect(db)
c = conn.cursor()

try:
    #c.execute("drop table carti_links")
    c.execute("drop table uzi_links")
except:
    # Nothing to drop, do nothing.
    pass


#cmd = "CREATE TABLE carti_links (link TEXT, datetime TEXT)"
cmd = "CREATE TABLE uzi_links (link TEXT, datetime TEXT)"

c.execute(cmd)


conn.commit()

conn.close()