# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:44:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-28 15:13:30
from flask import Blueprint,render_template

werewolf_api = Blueprint('werewolf_api', __name__)

@werewolf_api.route('/')
def home():
    return render_template("werewolf_home.html")

@werewolf_api.route('/setup')
def setup():
    return render_template("werewolf_setup.html")
