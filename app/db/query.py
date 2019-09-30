# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-30 16:11:31
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 17:45:03
# 通过用户名，获取用户记录，如果不存在，则返回None
users = [
    {'username': 'Tom', 'password': '111111','uid':'1','gid':'g1'},
    {'username': 'Michael', 'password': '123456','uid':'2','gid':'g2'}
]

def query_user(username):
    for user in users:
        if user['username'] == username:
            return user
    else:
        return None

def query_by_id(uid):
    for user in users:
        if user['uid'] == uid:
            return user
    else:
        return None
