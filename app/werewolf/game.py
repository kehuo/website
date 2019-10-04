# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 21:59:40
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 18:20:19

from app.werewolf.turn import Turn
from datetime import datetime, timedelta
from random import randint
from flask import current_app
from app.werewolf.db.tables import GameTable
from app.werewolf.enums import GameStatus, VictoryMode


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

    @classmethod
    def create_new_game(cls, host_id, victory_mode, roles):
        game_table = GameTable.create_new_game_table(host_id, victory_mode, roles)
        game = Game.create_game_from_table(game_table)
        return game

    @classmethod
    def create_game_from_table(cls, game_table):
        game = Game(gid=game_table.gid, host_id=game_table.host_id, status=GameStatus(game_table.status),
                    victory_mode=VictoryMode(game_table.victory_mode), users=None, turn=None,
                    roles=None, table=game_table)
        return game

    # def todict(self):

    #     d = {'gid': self.gid, 'host_id': self.host_id, 'status': self.status.value,
    #          'victory_mode': self.victory_mode.value, 'users': self.users, 'end_time': self.end_time,
    #          'last_modified': self.last_modified, 'turn': self.turn, 'roles': self.roles}
