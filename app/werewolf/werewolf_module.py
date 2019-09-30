# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:44:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 19:51:40
from flask import Blueprint, render_template, request, current_app, flash, redirect
from flask_login import current_user, login_required, login_user, logout_user
from app.db.query import query_user
from app.werewolf.user import User
from app.werewolf.game import Game

werewolf_api = Blueprint('werewolf_api', __name__)


@werewolf_api.route('/')
def home():
    return render_template("werewolf_home.html")


@werewolf_api.route('/setup')
@login_required
def setup():
    return render_template("werewolf_setup.html")


@werewolf_api.route('/game')
@login_required
def game():
    return render_template("werewolf_game.html", gid=current_user.game.gid)


def action():
    # get game
    pass


@werewolf_api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        user = query_user(username)
        current_app.logger.info(username + ' and ' + str(user))
        # 验证表单中提交的用户名和密码
        if user is not None and request.form['password'] == user['password']:
            curr_user = User()
            curr_user.id = user['uid']
            curr_user.game = Game(gid=user['gid'])

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user, remember=True)

            # 如果请求中有next参数，则重定向到其指定的地址，
            # 没有next参数，则重定向到"index"视图
            current_app.logger.info('login successfully')
            next = request.args.get('next')
            current_app.logger.info(next)
            return redirect(next or url_for('home'))
        else:
            flash('用户名或密码错误', 'error')
            return render_template('login.html')
    else:
        # GET 请求
        return render_template('login.html')


@werewolf_api.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'

@werewolf_api.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
