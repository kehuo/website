# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 22:05:35
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-06 14:36:21

from dataclasses import dataclass
from app.werewolf.game import Game
# from app.werewolf.player import Player
from flask_login import UserMixin
from app.werewolf.game import GameTable
from app.werewolf.role import Role
from datetime import datetime
from app.werewolf.db.connector import db


class UserTable(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(length=255), nullable=False, unique=True, index=True)
    password = db.Column(db.String(length=255), nullable=False)
    login_token = db.Column(db.String(length=255), index=True)
    name = db.Column(db.String(length=255), nullable=False)
    avatar = db.Column(db.Integer, nullable=False)
    gid = db.Column(db.Integer, nullable=False)
    player = db.Column(db.String(length=255))
    ishost = db.Column(db.Boolean, nullable=False)
    role = db.Column(db.String(length=255))
    position = db.Column(db.Integer, nullable=False)
    history = db.Column(db.String(length=255))


@dataclass
class User(UserMixin):
    uid: int = -1  # user id
    # username: str = ""
    # password: str = ""
    name: str = "New Player"
    avatar: int = 0
    game: Game = None
    # player: Player = None
    table: UserTable = None
    ishost: bool = False
    role: Role = None
    position: int = -1
    history: str = ""

    @classmethod
    def create_user_from_table(cls, user_table):
        user = User(uid=user_table.uid, name=user_table.name, avatar=user_table.avatar, table=user_table,
                    ishost=user_table.ishost, role=None, position=user_table.position, history=user_table.history)
        user.id = user_table.login_token
        user.game=Game.get_game_by_gid(user_table.gid)

        return user



