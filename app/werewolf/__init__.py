# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:43:45
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-02 15:53:05

from .werewolf_module import werewolf_api
from .login import init_login
from .db.connector import init_db


def init_app(app, prefix):
    app.register_blueprint(werewolf_api, url_prefix=prefix)
    init_login(app)
    init_db(app)
