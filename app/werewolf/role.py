# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 20:38:09
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 15:45:53

from dataclasses import dataclass
from app.werewolf.enums import RoleType, GroupType


@dataclass
class Role(object):
    """Base Class"""
    role_type: RoleType = RoleType.UNKNOWN
    group_type: GroupType = GroupType.UNKNOWN
    alive: bool = True
    iscaptain: bool = False
    votable: bool = True
    speakable: bool = True
