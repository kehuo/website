# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-19 17:55:24
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-22 19:07:18

from ml.ml_module import ml_api
from ml.predictor import init_predictor
from ml.markdown import init_md


def init_app(app):
    init_predictor()
    init_md(app)
