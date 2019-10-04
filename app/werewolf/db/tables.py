# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-02 15:44:15
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-02 18:12:26
from sqlalchemy.dialects.mysql import DATETIME
from app.werewolf.db.connector import db


class UserTable(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(length=255), nullable=False, unique=True, index=True)
    password = db.Column(db.String(length=255), nullable=False)
    login_token = db.Column(db.String(length=255),index=True)
    name = db.Column(db.String(length=255), nullable=False)
    avatar = db.Column(db.Integer, nullable=False)
    gid = db.Column(db.Integer, nullable=False)
    player = db.Column(db.String(length=255))
    ishost= db.Column(db.Boolean, nullable=False)
    role=db.Column(db.String(length=255))
    position=db.Column(db.Integer, nullable=False)
    history=db.Column(db.String(length=255))

    # uid: int = -1  # user id
    # name: str = "New Player"
    # password: str = ""
    # avatar: int = 0
    # game: Game = None
    # player: Player = None


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


# class PlayerTable(db.Model):
#     __tablename__='player'
#     nothing
