# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-06 22:08:14
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-07 18:14:21


class GameMessage(object):
    message_dict = {
        'GAME_NOT_EXIST': '房间不存在',
        'GAME_FULL': '房间已满',
        'ALREADY_IN': '你已在游戏中',
        'PLACE_HOLDER': '占位符'
    }

    def __init__(self, key, arg):
        assert(key in GameMessage.message_dict)
        self.key = key
        self.arg = arg

    def parse(self):
        if self.arg is None:
            return GameMessage.message_dict[self.key]
        else:
            return GameMessage.message_dict[self.key].format(*self.arg)
