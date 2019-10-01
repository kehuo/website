# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-01 14:23:05
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-01 17:42:39

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DATETIME


db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


class GameTable(db.Model):
    __tablename__ = 'game'
    gid = db.Column(db.Integer, primary_key=True, nullable=False)
    host_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    victory_mode = db.Column(db.Integer, nullable=False)
    players = db.Column(db.String(length=255))
    end_time = db.Column(DATETIME(fsp=3), nullable=False)
    last_modified = db.Column(DATETIME(fsp=3), nullable=False)
    turn = db.Column(db.String(length=255))
    roles = db.Column(db.String(length=255), nullable=False)

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            self.k = v

    def __repr__(self):
        return (f'Game item: gid={self.gid},host_id={self.host_id},status={self.status},'
                f'victory_mode={self.victory_mode},players={self.players},end_time={self.end_time},'
                f'last_modified={self.last_modified},turn={self.turn},roles={self.roles}')


# mysql=MySQL()

# # cur = mysql.connection.cursor()
# # cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
# # mysql.connection.commit()
# # cur.close()

# def init_db(app):
#     mysql.init_app(app)

# def execute(cmd):
#     cur = mysql.connection.cursor()
#     cur.execute(cmd)
#     rv = cur.fetchall()
#     cur.close()
#     return rv
#     # return str(rv)
