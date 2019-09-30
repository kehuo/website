# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:43:45
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 17:57:17
from .werewolf_module import werewolf_api
from flask_login import LoginManager
from app.werewolf.user import User
from app.db.query import query_by_id
from flask import current_app

login_manager = LoginManager()
login_manager.login_view = 'werewolf_api.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = "info"


# 如果用户名存在则构建一个新的用户类对象，并使用用户名作为ID
# 如果不存在，必须返回None


@login_manager.user_loader
def load_user(uid):
    current_app.logger.info('in load_user '+str(uid))
    user = query_by_id(uid)
    current_app.logger.info('in load_user '+str(user))
    if user is not None:
        curr_user = User()
        curr_user.id = user['uid']
        return curr_user
    else:
        return None
    # Must return None if uid not found

# 从请求参数中获取Token，如果Token所对应的用户存在则构建一个新的用户类对象
# 并使用用户名作为ID，如果不存在，必须返回None


@login_manager.request_loader
def load_user_from_request(request):
    current_app.logger.info('in load_user_from_request')
    uid = request.args.get('token')
    user = query_by_id(uid)
    if user is not None:
        curr_user = User()
        curr_user.id = user['uid']
        return curr_user
    else:
        return None
    # Must return None if uid not found


def init_app(app, prefix):
    app.register_blueprint(werewolf_api, url_prefix=prefix)
    login_manager.init_app(app)
    # init_login(app)
