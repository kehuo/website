# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-02 15:44:15
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-06 14:26:06

# from __future__ import annotations

# import json
# from app.werewolf.role import Role
# from app.werewolf.turn import Turn
# from datetime import datetime, timedelta
# from sqlalchemy.dialects.mysql import DATETIME
# from app.werewolf.db.connector import db
# from app.werewolf.enums import GameStatus, VictoryMode, CaptainMode, WitchMode
# import typing
# from typing import List
# from app.werewolf.turn import Turn
# from app.werewolf.json_utils import ExtendJSONEncoder
# # from app.werewolf.player import Player

# if typing.TYPE_CHECKING:
#     from app.werewolf.user import User


# class UserTable(db.Model):
#     __tablename__ = 'user'
#     uid = db.Column(db.Integer, primary_key=True, nullable=False)
#     username = db.Column(db.String(length=255), nullable=False, unique=True, index=True)
#     password = db.Column(db.String(length=255), nullable=False)
#     login_token = db.Column(db.String(length=255), index=True)
#     name = db.Column(db.String(length=255), nullable=False)
#     avatar = db.Column(db.Integer, nullable=False)
#     gid = db.Column(db.Integer, nullable=False)
#     player = db.Column(db.String(length=255))
#     ishost = db.Column(db.Boolean, nullable=False)
#     role = db.Column(db.String(length=255))
#     position = db.Column(db.Integer, nullable=False)
#     history = db.Column(db.String(length=255))

    # uid: int = -1  # user id
    # name: str = "New Player"
    # password: str = ""
    # avatar: int = 0
    # game: Game = None
    # player: Player = None


# class GameTable(db.Model):
#     __tablename__ = 'game'
#     gid = db.Column(db.Integer, primary_key=True, nullable=False)
#     host_id = db.Column(db.Integer, nullable=False)
#     status = db.Column(db.Integer, nullable=False)
#     victory_mode = db.Column(db.Integer, nullable=False)
#     captain_mode = db.Column(db.Integer, nullable=False)
#     witch_mode = db.Column(db.Integer, nullable=False)
#     users = db.Column(db.String(length=255))
#     end_time = db.Column(DATETIME(fsp=3), nullable=False)
#     last_modified = db.Column(DATETIME(fsp=3), nullable=False)
#     turn = db.Column(db.String(length=255))
#     roles = db.Column(db.String(length=255), nullable=False)

#     def __init__(self, gid: int, host_id: int, status: GameStatus, victory_mode: VictoryMode,
#                  users: List[User], end_time: datetime, turn: Turn, roles: List[Role],
#                  captain_mode: CaptainMode, witch_mode: WitchMode):
#         self.gid = gid
#         self.host_id = host_id
#         self.status = status.value
#         self.victory_mode = victory_mode.value
#         self.captain_mode = captain_mode.value
#         self.witch_mode = witch_mode.value
#         self.users = str([user.uid for user in users])
#         self.end_time = end_time
#         self.turn = json.dumps(turn, cls=ExtendJSONEncoder)
#         self.roles = json.dumps(roles)
#         # self.roles = json.dumps(roles, cls=ExtendJSONEncoder)

#     @classmethod
#     def create_new_game_table(cls, host_id: int, victory_mode: VictoryMode, roles: dict,
#                               captain_mode: CaptainMode, witch_mode: WitchMode):
#         turn = Turn(role_dict=roles, captain_mode=captain_mode)
#         game_table = GameTable(gid=None, host_id=host_id, status=GameStatus.WAIT_TO_START, victory_mode=victory_mode,
#                                users=[], end_time=datetime.utcnow() + timedelta(days=1), turn=turn, roles=roles,
#                                captain_mode=captain_mode, witch_mode=witch_mode)
#         return game_table

    # def __repr__(self):
    #     return (f'Game item: gid={self.gid},host_id={self.host_id},status={self.status},'
    #             f'victory_mode={self.victory_mode},users={self.users},end_time={self.end_time},'
    #             f'last_modified={self.last_modified},turn={self.turn},roles={self.roles}')


# class PlayerTable(db.Model):
#     __tablename__='player'
#     nothing
