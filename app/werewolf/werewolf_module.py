# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:44:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 13:37:23
from flask import Blueprint, render_template, request, current_app, flash, redirect
from flask_login import current_user, login_required
from app.werewolf.user import User
from app.werewolf.game import Game
from app.werewolf.db.tables import GameTable, UserTable
import time
import json
from app.werewolf.login import do_login, do_logout,do_register

werewolf_api = Blueprint('werewolf_api', __name__)


@werewolf_api.route('/')
def home():
    return render_template("werewolf_home.html")


@werewolf_api.route('/setup', methods=['GET', 'POST'])
@login_required
def setup():
    if request.method == 'GET':
        return render_template("werewolf_setup.html")
    else:
        game = Game()


@werewolf_api.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    if request.method == 'GET':
        me = GameTable.query.get(11)
        return render_template("werewolf_game.html", gid=current_user.game.gid, dbtxt=(me, type(me)))


def action():
    # get game
    pass


@werewolf_api.route('/login', methods=['GET', 'POST'])
def login():
    return do_login()


@werewolf_api.route('/logout')
@login_required
def logout():
    return do_logout()


@werewolf_api.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
