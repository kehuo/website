# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-22 15:57:01
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-22 18:35:34
from website import create_app

app_ins = create_app('development')


if __name__ == '__main__':
    app_ins.run(port=app_ins.config['PORT'])
