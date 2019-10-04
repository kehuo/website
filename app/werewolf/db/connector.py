# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-10-01 14:23:05
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-02 15:45:17

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
