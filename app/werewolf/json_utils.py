# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-05 16:03:18
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-06 11:18:24
import json

from functools import singledispatch
from app.werewolf.turn import Turn
from enum import Enum
from flask import current_app


@singledispatch
def convert(o):
    raise TypeError('not special type')


@convert.register(Enum)
def _(o):
    return o.name


@convert.register(Turn)
def _(o):
    return o.__dict__

# @convert.register(datetime)
# def _(o):
#     return o.strftime('%b %d %Y %H:%M:%S')

# @convert.register(Decimal)
# def _(o):
#     return float(o)

# @convert.register(MyClass)
# def _(o):
#     return o.get_value()


class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return convert(obj)
        except TypeError:
            return super().default(obj)


def JsonHook(cls=None):
    def hook(d):
        if cls is not None:
            obj = cls()
            obj.__dict__ = d
            return obj
        else:
            return d
    return hook
