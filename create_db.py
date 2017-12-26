#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "dict")
cursor = db.cursor()

with open("dict.txt", 'r') as f:
    sql = "INSERT INTO `dict` ( `word`) VALUES (%s)"
    param = []
    for line in f.readlines():
        index = line.find("/")
        if index > 0:
            word = line[:index].strip()
            param.append(word)

    try:
        cursor.executemany(sql, param)
        db.commit()
        print 'success'
    except:
        db.rollback()
        print 'error'

    db.close()
