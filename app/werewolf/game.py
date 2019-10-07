# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 21:59:40
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-07 18:14:59

from __future__ import annotations


from app.werewolf.turn import Turn
from datetime import datetime, timedelta
from random import randint
from flask import current_app
from app.werewolf.enums import GameStatus, VictoryMode, CaptainMode, WitchMode, RoleType
import json
from app.werewolf.json_utils import JsonHook, ExtendJSONEncoder
from app.werewolf.db.connector import db
from app.werewolf.role import Role
from sqlalchemy.dialects.mysql import DATETIME
import typing
from typing import List
from app.werewolf.game_message import GameMessage
from collections import Counter
from app.werewolf.role import Role

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
    roles = db.Column(db.String(length=255))
    end_time = db.Column(DATETIME(fsp=3), nullable=False)
    last_modified = db.Column(DATETIME(fsp=3), nullable=False)
    turn = db.Column(db.String(length=1023))
    card_dict = db.Column(db.String(length=1023), nullable=False)
    audio = db.Column(db.String(length=4095), nullable=False)
    history = db.Column(db.String(length=4095), nullable=False)

    def __init__(self, host_id: int, victory_mode: VictoryMode, roles: List[Role], end_time: datetime, turn: Turn, card_dict: dict,
                 captain_mode: CaptainMode, witch_mode: WitchMode, audio: dict, history: dict, gid: int = None,
                 status: GameStatus = GameStatus.WAIT_TO_START):
        self.gid = gid
        self.host_id = host_id
        self.status = status.value
        self.victory_mode = victory_mode.value
        self.captain_mode = captain_mode.value
        self.witch_mode = witch_mode.value
        if roles is None:
            roles = []
        self.roles = json.dumps([role.uid for role in roles], cls=ExtendJSONEncoder)
        self.end_time = end_time
        self.turn = json.dumps(turn, cls=ExtendJSONEncoder)
        self.card_dict = json.dumps(card_dict, cls=ExtendJSONEncoder)
        self.audio = json.dumps(audio, cls=ExtendJSONEncoder)
        self.history = json.dumps(history, cls=ExtendJSONEncoder)
        # self.roles = json.dumps(roles, cls=ExtendJSONEncoder)

    @classmethod
    def create_new_game_table(cls, host_id: int, victory_mode: VictoryMode, card_dict: dict,
                              captain_mode: CaptainMode, witch_mode: WitchMode):
        turn = Turn(card_dict=card_dict, captain_mode=captain_mode)
        game_table = GameTable(host_id=host_id, victory_mode=victory_mode,
                               roles=[], end_time=datetime.utcnow() + timedelta(days=1), turn=turn, card_dict=card_dict,
                               captain_mode=captain_mode, witch_mode=witch_mode, audio={'toget': 0, 'queue': []},
                               history={'toget': 0, 'queue': []})
        return game_table


class Game(object):
    def __init__(self, gid: int = -1, host_id: int = -1, status: GameStatus = GameStatus.UNKNOWN,
                 victory_mode: VictoryMode = VictoryMode.UNKNOWN, roles: list = None,
                 turn: Turn = None, card_dict: dict = None, audio: dict = None, history: dict = None, table: GameTable = None):
        self.gid = gid
        self.host_id = host_id  # host's uid
        self.status = status
        # active: list = list  # who can act???
        self.victory_mode = victory_mode
        if roles is None:
            self.roles = []
        else:
            self.roles = roles
        # self.end_time = end_time  # the limit of this game
        # self.last_modified = last_modified  # the time stamp of last operation on this game
        self.turn = turn
        if card_dict is None:
            self.card_dict = {}
        else:
            self.card_dict = card_dict
        if audio is None:
            self.audio = {'toget': 0, 'queue': []}
        else:
            self.audio = audio
        if history is None:
            self.history = {'toget': 0, 'queue': []}
        else:
            self.history = history

        self.table = table

    def __setattr__(self, name, value):
        if hasattr(self, 'table') and self.table is not None and name != 'table':
            if name in ['status', 'victory_mode', 'captain_mode', 'witch_mode']:
                self.table.__setattr__(name, value.value)
            elif name in ['turn', 'card_dict', 'audio', 'history']:
                self.table.__setattr__(name, json.dumps(value, cls=ExtendJSONEncoder))
            elif name == 'roles':
                self.table.__setattr__(name, str([role.uid for role in value]))
            else:
                self.table.__setattr__(name, value)
        return super().__setattr__(name, value)

    @classmethod
    def create_new_game(cls, host: User, victory_mode: VictoryMode, card_dict: dict, captain_mode: CaptainMode, witch_mode: WitchMode):
        game_table = GameTable.create_new_game_table(host_id=host.uid, victory_mode=victory_mode, card_dict=card_dict,
                                                     captain_mode=captain_mode, witch_mode=witch_mode)
        db.session.add(game_table)
        db.session.commit()
        game = Game.create_game_from_table(game_table)
        return game

    @classmethod
    def create_game_from_table(cls, game_table):
        uids = json.loads(game_table.roles, object_hook=JsonHook())
        roles = []
        for uid in uids:
            new_role = Role.get_role_by_uid(uid)
            roles.append(new_role)

        game = Game(gid=game_table.gid, host_id=game_table.host_id, status=GameStatus(game_table.status),
                    victory_mode=VictoryMode(game_table.victory_mode), roles=roles,
                    turn=json.loads(game_table.turn, object_hook=JsonHook(Turn)),
                    card_dict=json.loads(game_table.card_dict, object_hook=JsonHook()),
                    audio=json.loads(game_table.audio, object_hook=JsonHook()),
                    history=json.loads(game_table.history, object_hook=JsonHook()), table=game_table)
        return game

    @classmethod
    def get_game_by_gid(cls, gid):
        if gid == -1:
            return None

        game_table = GameTable.query.get(gid)
        if game_table and datetime.utcnow() < game_table.end_time:
            return Game.create_game_from_table(game_table)
        else:
            return None

    def commit(self, lock=False, func=None)->(bool, str):
        if not lock:
            db.session.add(self.table)
            db.session.commit()
            return True, None
        else:
            new_table = GameTable.query.with_for_update().get(self.gid)
            if new_table is None:
                return False, GameMessage('GAME_NOT_EXIST', None)
            else:
                self.table = new_table
                success, message = func(self)
                db.session.commit()
                return success, message

    def get_seat_num(self):
        cnt = sum(Counter(self.card_dict).values())
        if RoleType.THIEF.name in self.card_dict:
            cnt -= 2
        return cnt

    def get_role_by_pos():
        pass

    def get_role_by_uid(self, uid):
        for r in self.roles:
            if r.uid == uid:
                return r
        else:
            return None

    # if not user_table.login_token:
        #     user_table.login_token = get_login_token(username)
        #     db.session.commit()
        # else:
        #     # 已经登录了
        #     current_app.logger.info(user_table.login_token)
        #     return redirect(url_for('werewolf_api.logout'))
