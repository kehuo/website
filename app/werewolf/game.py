# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 21:59:40
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-01 17:39:35

from enum import Enum, auto
from app.werewolf.turn import Turn
from datetime import datetime, timedelta
from random import randint
from flask import current_app


class GameStatus(Enum):
    UNKNOWN = 0
    WAIT_TO_START = auto()
    DAY = auto()
    NIGHT = auto()
    ELECTING = auto()
    VOTING = auto()
    WAITING = auto()


class VictoryMode(Enum):
    UNKNOWN = 0
    KILL_GROUP = auto()  # 屠边
    KILL_ALL = auto()  # 屠城


class Game(object):
    def __init__(self, gid: int = -1, host_id: int = -1, status: GameStatus = GameStatus.UNKNOWN,
                 victory_mode: VictoryMode = VictoryMode.UNKNOWN, players: list = [None],
                 end_time: datetime = datetime.utcnow, last_modified: datetime = datetime.utcnow,
                 turn: Turn = None, roles: list = []):
        self.gid = gid
        self.host_id = host_id  # host's uid
        self.status = status
        # active: list = list  # who can act???
        self.victory_mode = victory_mode
        self.players = players  # pos 0 is None, player starts from pos 1
        self.end_time = end_time  # the limit of this game
        self.last_modified = last_modified  # the time stamp of last operation on this game
        self.turn = turn
        self.roles = roles

    @classmethod
    def create_game(self, host_id, victory_mode, roles):
        game = Game(host_id=host_id, victory_mode=victory_mode, roles=roles, status=GameStatus.WAIT_TO_START, turn=Turn())
        game.end_time = datetime.utcnow() + timedelta(days=1)
        game.last_modified = datetime.utcnow()
        return game

        for _ in range(current_app.config['MAX_TRY']):
            pass
