# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:44:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-05 22:50:09
from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from flask_login import current_user, login_required
from app.werewolf.user import User
from app.werewolf.game import Game
from app.werewolf.db.tables import GameTable, UserTable
import time
import json
from app.werewolf.login import do_login, do_logout, do_register
from app.werewolf.enums import VictoryMode, RoleType, CaptainMode, WitchMode
from app.werewolf.db.connector import db


werewolf_api = Blueprint('werewolf_api', __name__)


@werewolf_api.route('/')
def home():
    return render_template("werewolf_home.html")


@werewolf_api.route('/setup', methods=['GET', 'POST'])
@login_required
def setup():
    if request.method == 'GET':
        # TODO: ask to quick existing game if user is in a game!
        return render_template("werewolf_setup.html")
    else:
        victory_mode = VictoryMode[request.form['victoryMode'].upper()]
        captain_mode = CaptainMode[request.form['captainMode'].upper()]
        witch_mode = WitchMode[request.form['witchMode'].upper()]
        villager_cnt = int(request.form['villager'])
        normal_wolf_cnt = int(request.form['normal_wolf'])
        roles = {RoleType.VILLAGER.name: villager_cnt, RoleType.NORMAL_WOLF.name: normal_wolf_cnt}

        single_roles = request.form.getlist('single_roles')
        for r in single_roles:
            roles[r.upper()] = 1

        game = Game.create_new_game(current_user.uid, victory_mode, roles, captain_mode, witch_mode)
        # db.session.add(game.table)
        # # db.session.flush()
        # db.session.commit()
        # game.gid = game.table.gid
        # TODO: position, ishost
        current_user.game = game
        current_user.table.gid = game.gid
        # current_app.logger.info(game.gid)
        db.session.add(current_user.table)
        db.session.commit()

        return redirect(url_for('werewolf_api.game'))


@werewolf_api.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    if request.method == 'GET':
        return render_template("werewolf_game.html", ishost=current_user.ishost,
                               gid=current_user.game.gid, dbtxt=(current_user.game.table.roles + '\n<br />\n' + str(current_user.game.turn)+ str(type(current_user.game.turn))))


@werewolf_api.route('/game_process')
@login_required
def game_process():
    pass


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
