# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 14:38:30
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-04 13:37:50

from flask import render_template, request,redirect,url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from app.werewolf.user import User
from app.werewolf.game import Game, GameStatus, VictoryMode
# from app.werewolf.player import Player
from flask import current_app
from app.werewolf.db.tables import UserTable, GameTable
from datetime import datetime
from hashlib import sha1
from app.werewolf.db.connector import db


def get_login_token(username):
    return sha1((current_app.config["LOGIN_SECRET_KEY"]+username+str(datetime.utcnow().timestamp())).encode('utf-8')).hexdigest()


def init_login(app):
    login_manager = LoginManager(app)
    login_manager.login_view = 'werewolf_api.login'
    login_manager.login_message = '请先登录'
    login_manager.login_message_category = "info"

    def _get_user_from_db(login_token):
        if not login_token:
            return None
        user_table = UserTable.query.filter_by(login_token=login_token).first()
        if user_table is not None:
            return User.create_user_from_table(user_table)
        else:
            return None

    @login_manager.user_loader
    def load_user(login_token):
        return _get_user_from_db(login_token)

    @login_manager.request_loader
    def load_user_from_request(request):
        login_token = request.args.get('token')
        return _get_user_from_db(login_token)


def do_login():
    if request.method == 'POST':
        username = request.form.get('username')
        # 避免用户手抖点击登录两次
        # user_table = UserTable.query.filter_by(username=username).with_for_update().first()
        user_table = UserTable.query.filter_by(username=username).first()

        current_app.logger.info(f'get user with username= {username}, found= {user_table is not None}')
        if user_table and request.form['password'] == user_table.password:
            # if not user_table.login_token:
            #     user_table.login_token = get_login_token(username)
            #     db.session.commit()
            # else:
            #     # 已经登录了
            #     current_app.logger.info(user_table.login_token)
            #     return redirect(url_for('werewolf_api.logout'))
            user_table.login_token = get_login_token(username)
            db.session.add(user_table)
            db.session.commit()

            user = User.create_user_from_table(user_table)
            # 通过Flask-Login的login_user方法登录用户
            login_user(user, remember=True)
            # 如果请求中有next参数，则重定向到其指定的地址，
            # 没有next参数，则重定向到"home"视图
            current_app.logger.info(f'{username} login successfully!')
            next = request.args.get('next')
            return redirect(next or url_for('werewolf_api.home'))
        else:
            current_app.logger.info(f'{username} login failed!')
            flash('用户名或密码错误', 'error')
            return render_template('login.html')
    else:
        # GET 请求
        return render_template('login.html')


def do_logout():
    username = current_user.name
    current_user.table.login_token = ""
    db.session.add(current_user.table)
    db.commit()
    logout_user()
    current_app.logger.info(f'{username} logout successfully!')
    # try:
    # except Exception as e:
    #     current_app.logger.info(str(e))

    return 'Logged out successfully!'


def do_register():
    existing_user = UserTable.query.filter_by(username=username).first()
    if existing_user:
        flash('用户名已存在', 'error')
        return render_template('login.html')

# # @login_manager.unauthorized_handler
# # def unauthorized_handler():
# #     return 'Unauthorized'


# # app.secret_key = '1234567'


# user=UserTable.query.filter_by(login_token=login_token).with_for_update().first()
# if addr.status == 0:
# addr.status = 1
# db.session.commit()
