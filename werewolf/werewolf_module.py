# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:44:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-16 17:55:09
from flask import Blueprint

werewolf_api = Blueprint('werewolf_api', __name__)

@werewolf_api.route('/')
def home():
    return '<h1>Hello, this is werewolf blueprint</h1>'
