# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-28 22:05:35
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 14:24:29

from dataclasses import dataclass
from app.werewolf.game import Game
from app.werewolf.player import Player
from flask_login import UserMixin


@dataclass
class User(UserMixin):
    uid: int = -1  # user id
    name: str = "New Player"
    avatar: int = 0
    game: Game = None
    player: Player = None
