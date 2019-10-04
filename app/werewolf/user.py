# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 22:05:35
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 18:42:51

from dataclasses import dataclass
from app.werewolf.game import Game
# from app.werewolf.player import Player
from flask_login import UserMixin
from app.werewolf.db.tables import UserTable, GameTable
from app.werewolf.role import Role
from datetime import datetime


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
        if user_table.gid != -1:
            game_table = GameTable.query.get(user_table.gid)
            # if game_table and datetime.utcnow() < datetime.strptime(game_table.end_time):
            if game_table and datetime.utcnow() < game_table.end_time:
                game = Game.create_game_from_table(game_table)
                user.game = game
        return user
