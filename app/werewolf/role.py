# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 20:38:09
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-28 21:58:48

from enum import Enum, auto
from dataclasses import dataclass


class RoleType(Enum):
    UNKNOWN = 0
    SEER = auto()
    HUNTER = auto()
    CUPID = auto()
    WITCH = auto()
    LITTLE_GIRL = auto()
    THIEF = auto()
    VILLAGER = auto()
    NORMAL_WOLF = auto()
    IDIOT = auto()
    ANCIENT = auto()
    SCAPEGOAT = auto()
    SAVIOR = auto()
    PIPER = auto()
    WHITE_WOLF = auto()
    RAVEN = auto()
    PYROMANIAC = auto()
    TWO_SISTERS = auto()
    THREE_BROTHERS = auto()
    ANGEL = auto()


class GroupType(Enum):
    UNKNOWN = 0
    WOLVES = auto()
    GODS = auto()
    VILLAGERS = auto()
    THIRD_PARTY = auto()


@dataclass
class Role(object):
    """Base Class"""
    role_type: RoleType = RoleType.UNKNOWN
    group_type: GroupType = GroupType.UNKNOWN
    alive: bool = True
    iscaptain: bool = False
    votable: bool = True
    speakable: bool = True
