# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 22:41:11
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-01 17:33:14
import sys
sys.path.append('..')




# from app import create_app

# app_ins = create_app('development')

# from app.db.db_connector import execute

# print(execute("select * from test where 'key'='audio'"))

from datetime import datetime, timedelta
from enum import Enum, auto



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
                 turn = None, roles: list = []):
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
    def create_game(self,host_id, victory_mode, roles):
        game = Game(host_id=host_id, victory_mode=victory_mode, roles=roles, status=GameStatus.WAIT_TO_START, turn=None)
        game.end_time = datetime.utcnow() + timedelta(days=1)
        game.last_modified = datetime.utcnow()
        return game



me=Game.create_game(1,11,[1,2,3])
print(me.__dict__)



from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DATETIME


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
you=GameTable(me.__dict__)
print(you)
