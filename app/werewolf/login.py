# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 14:38:30
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 17:26:38

# from flask_login import LoginManager
# from app.werewolf.user import User
# # from app.db.query import query_user


# # 通过用户名，获取用户记录，如果不存在，则返回None
# def query_user(username):
#     users = [
#         {'username': 'Tom', 'password': '111111','uid':1,'gid':'g1'},
#         {'username': 'Michael', 'password': '123456','uid':2,'gid':'g2'}
#     ]
#     for user in users:
#         if user['username'] == username:
#             return user
#     else:
#         return None

# def init_login(app):
#     # app.secret_key = '1234567'

#     login_manager = LoginManager(app)
#     login_manager.login_view = 'werewolf_api.login'
#     # login_manager.login_message = 'Unauthorized User'
#     login_manager.login_message_category = "info"


#     # 如果用户名存在则构建一个新的用户类对象，并使用用户名作为ID
#     # 如果不存在，必须返回None


#     @login_manager.user_loader
#     def load_user(username):
#         user = query_user(username)
#         if user is not None:
#             curr_user = User()
#             curr_user.id = user['uid']
#             return curr_user
#         else:
#             return None
#         # Must return None if username not found

#     # 从请求参数中获取Token，如果Token所对应的用户存在则构建一个新的用户类对象
#     # 并使用用户名作为ID，如果不存在，必须返回None


#     @login_manager.request_loader
#     def load_user_from_request(request):
#         username = request.args.get('token')
#         user = query_user(username)
#         if user is not None:
#             curr_user = User()
#             curr_user.id = user['uid']
#             return curr_user
#         else:
#             return None
#         # Must return None if username not found

# # @login_manager.unauthorized_handler
# # def unauthorized_handler():
# #     return 'Unauthorized'


# # @app.route('/')
# # @login_required
# # def index():
# #     return render_template('hello.html')


# # @app.route('/home')
# # @fresh_login_required
# # def home():
# #     return 'Logged in as: %s' % current_user.get_id()



# # app.secret_key = '1234567'

