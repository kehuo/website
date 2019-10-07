# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 20:38:09
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-07 16:49:05

from dataclasses import dataclass
from app.werewolf.db.connector import db
from app.werewolf.enums import RoleType, GroupType


class RoleTable(db.Model):
    __tablename__ = 'role'
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    role_type = db.Column(db.Integer)
    group_type = db.Column(db.Integer)
    alive = db.Column(db.Boolean)
    iscaptain = db.Column(db.Boolean)
    votable = db.Column(db.Boolean)
    speakable = db.Column(db.Boolean)
    position = db.Column(db.Integer)
    history = db.Column(db.String(length=4095))

    def __init__(self, uid: int, role_type: RoleType = RoleType.UNKNOWN, group_type: GroupType = GroupType.UNKNOWN,
                 alive: bool = True, iscaptain: bool = False, votable: bool = True, speakable: bool = True,
                 position: int = -1, history: str = ""):
        self.uid = uid
        self.role_type = role_type.value
        self.group_type = group_type.value
        self.alive = alive
        self.iscaptain = iscaptain
        self.votable = votable
        self.speakable = speakable
        self.position = position
        self.history = history

    def _reset(self):
        self.role_type = RoleType.UNKNOWN.value
        self.group_type = GroupType.UNKNOWN.value
        self.alive = True
        self.iscaptain = False
        self.votable = True
        self.speakable = True
        self.position = -1
        self.history = ""


@dataclass
class Role(object):
    """Base Class"""
    uid: int = -1  # user id
    role_type: RoleType = RoleType.UNKNOWN
    group_type: GroupType = GroupType.UNKNOWN
    alive: bool = True
    iscaptain: bool = False
    votable: bool = True
    speakable: bool = True
    position: int = -1
    history: str = ""
    table: RoleTable = None

    def __setattr__(self, name, value):
        if hasattr(self, 'table') and self.table is not None and name in self.__dict__ and name not in ['table']:
            if name in ['role_type', 'group_type']:
                self.table.__setattr__(name, value.value)
            else:
                self.table.__setattr__(name, value)
        return super().__setattr__(name, value)

    def _reset(self):
        self.role_type = RoleType.UNKNOWN
        self.group_type = GroupType.UNKNOWN
        self.alive = True
        self.iscaptain = False
        self.votable = True
        self.speakable = True
        self.position = -1
        self.history = ""

    @classmethod
    def create_role_from_table(cls, role_table):
        role = Role(uid=role_table.uid, role_type=RoleType(role_table.role_type), group_type=GroupType(role_table.group_type),
                    alive=role_table.alive, iscaptain=role_table.iscaptain, votable=role_table.votable, speakable=role_table.speakable,
                    position=role_table.position, history=role_table.history, table=role_table)
        return role

    @classmethod
    def create_new_role(cls, uid):
        role_table = RoleTable.query.get(uid)
        if role_table is None:
            role_table = RoleTable(uid=uid)
        else:
            role_table._reset()
        db.session.add(role_table)
        db.session.commit()
        role = Role.create_role_from_table(role_table)
        return role

    @classmethod
    def get_role_by_uid(cls, uid):
        role_table = RoleTable.query.get(uid)
        if role_table is not None:
            return Role.create_role_from_table(role_table)
        else:
            return None

    def commit(self):
        db.session.add(self.table)
        db.session.commit()
