# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-16 17:43:45
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-10-02 15:53:05

import os
import sys

blueprints_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blueprints')
sys.path.append(os.path.join(blueprints_path, 'werewolf'))
sys.path.append(os.path.join(blueprints_path, 'ml'))

from flask import Flask, render_template  # noqa: E402
from werewolf import werewolf_api, init_app as init_werewolf  # noqa: E402
# from ml import ml_api, init_app as init_ml  # noqa: E402

from website.config import config  # noqa: E402


def init_app(app):
    init_werewolf(app)
    # init_ml(app)


def create_app(config_name=None):
    # create and configure the app
    root_path = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__, instance_relative_config=True, root_path=root_path,
                instance_path=os.path.join(root_path, 'instance'))
    if config_name:
        app.config.from_object(config[config_name])
    else:
        app.config.from_pyfile('config.py', silent=True)

    if app.config["DEBUG"]:
        @app.after_request
        def after_request(response):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
            response.headers["Expires"] = 0
            response.headers["Pragma"] = "no-cache"
            return response

    app.register_blueprint(werewolf_api, url_prefix='/werewolf')
    # app.register_blueprint(ml_api,url_prefix='/ml')
    init_app(app)

    @app.route('/')
    def homepage():
        return render_template('index.html')

    return app
