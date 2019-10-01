# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 16:11:15
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-01 15:31:24
from .connector import init_db

def init_app(app):
    init_db(app)
