# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-04 15:43:49
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 15:45:36

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
