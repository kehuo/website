# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 22:16:51
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 23:14:09
from flask_mysqldb import MySQL

mysql=MySQL()

# cur = mysql.connection.cursor()
# cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
# mysql.connection.commit()
# cur.close()

def init_db(app):
    mysql.init_app(app)

def execute(cmd):
    cur = mysql.connection.cursor()
    cur.execute(cmd)
    rv = cur.fetchall()
    cur.close()
    return rv
    # return str(rv)
