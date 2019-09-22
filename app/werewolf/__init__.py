# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:43:45
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-22 17:26:51
from .werewolf_module import werewolf_api


def init_app(app, prefix):
    app.register_blueprint(werewolf_api, url_prefix=prefix)
