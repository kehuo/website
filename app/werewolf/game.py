# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 21:59:40
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 14:23:38

from dataclasses import dataclass
from enum import Enum,auto


class GameStatus(Enum):
    UNKNOWN = 0
    WAIT_TO_START = auto()
    DAY = auto()
    NIGHT = auto()
    ELECTING = auto()
    VOTING = auto()
    WAITING = auto()


@dataclass
class Game(object):
    gid: int = -1
    host_id: int = -1  # host's uid
    turn: int = -1
    status: GameStatus = GameStatus.UNKNOWN
    active: list = list  # who can act
