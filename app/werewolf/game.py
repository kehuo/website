# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 21:59:40
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-06 14:39:02

from __future__ import annotations


from app.werewolf.turn import Turn
from datetime import datetime, timedelta
from random import randint
from flask import current_app
from app.werewolf.enums import GameStatus, VictoryMode, CaptainMode, WitchMode
import json
from app.werewolf.json_utils import JsonHook, ExtendJSONEncoder
from app.werewolf.db.connector import db
from app.werewolf.role import Role
from sqlalchemy.dialects.mysql import DATETIME
import typing
from typing import List


if typing.TYPE_CHECKING:
    from app.werewolf.user import User


class GameTable(db.Model):
    __tablename__ = 'game'
    gid = db.Column(db.Integer, primary_key=True, nullable=False)
    host_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    victory_mode = db.Column(db.Integer, nullable=False)
    captain_mode = db.Column(db.Integer, nullable=False)
    witch_mode = db.Column(db.Integer, nullable=False)
    users = db.Column(db.String(length=255))
    end_time = db.Column(DATETIME(fsp=3), nullable=False)
    last_modified = db.Column(DATETIME(fsp=3), nullable=False)
    turn = db.Column(db.String(length=255))
    roles = db.Column(db.String(length=255), nullable=False)

    def __init__(self, gid: int, host_id: int, status: GameStatus, victory_mode: VictoryMode,
                 users: List[User], end_time: datetime, turn: Turn, roles: List[Role],
                 captain_mode: CaptainMode, witch_mode: WitchMode):
        self.gid = gid
        self.host_id = host_id
        self.status = status.value
        self.victory_mode = victory_mode.value
        self.captain_mode = captain_mode.value
        self.witch_mode = witch_mode.value
        self.users = str([user.uid for user in users])
        self.end_time = end_time
        self.turn = json.dumps(turn, cls=ExtendJSONEncoder)
        self.roles = json.dumps(roles)
        # self.roles = json.dumps(roles, cls=ExtendJSONEncoder)

    @classmethod
    def create_new_game_table(cls, host_id: int, victory_mode: VictoryMode, roles: dict,
                              captain_mode: CaptainMode, witch_mode: WitchMode):
        turn = Turn(role_dict=roles, captain_mode=captain_mode)
        game_table = GameTable(gid=None, host_id=host_id, status=GameStatus.WAIT_TO_START, victory_mode=victory_mode,
                               users=[], end_time=datetime.utcnow() + timedelta(days=1), turn=turn, roles=roles,
                               captain_mode=captain_mode, witch_mode=witch_mode)
        return game_table


class Game(object):
    def __init__(self, gid: int = -1, host_id: int = -1, status: GameStatus = GameStatus.UNKNOWN,
                 victory_mode: VictoryMode = VictoryMode.UNKNOWN, users: list = [None],
                 end_time: datetime = datetime.utcnow, last_modified: datetime = datetime.utcnow,
                 turn: Turn = None, roles: list = [], table: GameTable = None):
        self.gid = gid
        self.host_id = host_id  # host's uid
        self.status = status
        # active: list = list  # who can act???
        self.victory_mode = victory_mode
        self.users = users  # pos 0 is None, player starts from pos 1
        # self.end_time = end_time  # the limit of this game
        # self.last_modified = last_modified  # the time stamp of last operation on this game
        self.turn = turn
        self.roles = roles
        self.table = table

    def __setattr__(self, name, value):
        if hasattr(self, 'table') and self.table is not None and name != 'table':
            if name in ['status', 'victory_mode']:
                self.table.__setattr__(name, value.name)
            elif name == 'turn':
                self.table.__setattr__(name, json.dumps(value, cls=ExtendJSONEncoder))
            else:
                self.table.__setattr__(name, value)
        return super().__setattr__(name, value)

    @classmethod
    def create_new_game(cls, host_id, victory_mode, roles, captain_mode, witch_mode):
        game_table = GameTable.create_new_game_table(host_id, victory_mode, roles, captain_mode, witch_mode)
        db.session.add(game_table)
        db.session.commit()
        game = Game._create_game_from_table(game_table)
        return game

    @classmethod
    def _create_game_from_table(cls, game_table):
        game = Game(gid=game_table.gid, host_id=game_table.host_id, status=GameStatus(game_table.status),
                    victory_mode=VictoryMode(game_table.victory_mode), users=None,
                    turn=json.loads(game_table.turn, object_hook=JsonHook(Turn)), roles=None, table=game_table)
        return game

    @classmethod
    def get_game_by_gid(cls, gid):
        if gid == -1:
            return None

        game_table = GameTable.query.get(gid)
        if game_table and datetime.utcnow() < game_table.end_time:
            return Game._create_game_from_table(game_table)
        else:
            return None

    def commit(self):
        db.session.add(self.table)
        db.session.commit()

    # def todict(self):

    #     d = {'gid': self.gid, 'host_id': self.host_id, 'status': self.status.value,
    #          'victory_mode': self.victory_mode.value, 'users': self.users, 'end_time': self.end_time,
    #          'last_modified': self.last_modified, 'turn': self.turn, 'roles': self.roles}
