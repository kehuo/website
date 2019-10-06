# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 22:05:35
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-06 20:40:38

from dataclasses import dataclass
from app.werewolf.game import Game
# from app.werewolf.player import Player
from flask_login import UserMixin
from app.werewolf.game import GameTable
from app.werewolf.role import Role
from datetime import datetime
from app.werewolf.db.connector import db
import json
from app.werewolf.json_utils import JsonHook, ExtendJSONEncoder


class UserTable(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(length=255), nullable=False, unique=True, index=True)
    password = db.Column(db.String(length=255), nullable=False)
    login_token = db.Column(db.String(length=255), index=True)
    name = db.Column(db.String(length=255), nullable=False)
    avatar = db.Column(db.Integer, nullable=False)
    gid = db.Column(db.Integer, nullable=False)
    # player = db.Column(db.String(length=255))
    ishost = db.Column(db.Boolean, nullable=False)
    role = db.Column(db.String(length=255))
    position = db.Column(db.Integer, nullable=False)
    history = db.Column(db.String(length=255))

    def __init__(self, uid: int = None, username: str = None, password: str = None, login_token: str = None, name: str = None,
                 avatar: int = -1, gid: int = -1, ishost: bool = False, role: Role = None, position: int = -1, history: str = ""):
        self.uid = uid
        self.username = username
        self.password = password
        self.login_token = login_token
        self.name = name
        self.avatar = avatar
        self.gid = gid
        self.ishost = ishost
        self.role = json.dumps(role, cls=ExtendJSONEncoder)
        self.position = position
        self.history = history

    @classmethod
    def create_new_user_table(cls, username, password, name, avatar):
        user_table = UserTable(username=username, password=password, name=name, avatar=avatar)
        return user_table


@dataclass
class User(UserMixin):
    uid: int = -1  # user id
    # username: str = ""
    # password: str = ""
    name: str = "New Player"
    avatar: int = 0
    game: Game = None
    # player: Player = None
    ishost: bool = False
    role: Role = None
    position: int = -1
    history: str = ""
    table: UserTable = None

    def __setattr__(self, name, value):
        if hasattr(self, 'table') and self.table is not None and name in self.__dict__ and name not in ['table', 'id']:
            if name == 'game' and value is not None:
                self.table.__setattr__('gid', value.gid)
            elif name == 'role':
                self.table.__setattr__(name, json.dumps(value, cls=ExtendJSONEncoder))
            else:
                self.table.__setattr__(name, value)
        return super().__setattr__(name, value)

    @classmethod
    def create_user_from_table(cls, user_table):
        user = User(uid=user_table.uid, name=user_table.name, avatar=user_table.avatar, table=user_table,
                    ishost=user_table.ishost, role=None, position=user_table.position, history=user_table.history)
        user.id = user_table.login_token
        user.game = Game.get_game_by_gid(user_table.gid)

        return user

    @classmethod
    def create_new_user(cls, username, password, name, avatar):
        if UserTable.query.filter_by(username=username).first() is not None:
            # username exists
            return None
        user_table = UserTable(username=username, password=password, name=name, avatar=avatar)
        db.session.add(user_table)
        db.session.commit()
        user = User.create_user_from_table(user_table)
        return user

    @classmethod
    def get_user_by_uid(cls, uid):
        user_table = UserTable.query.get(uid)
        if user_table is not None:
            return User.create_user_from_table(user_table)
        else:
            return None

    @classmethod
    def get_user_by_token(cls, login_token):
        if not login_token:
            return None
        user_table = UserTable.query.filter_by(login_token=login_token).first()
        if user_table is not None:
            return User.create_user_from_table(user_table)
        else:
            return None
