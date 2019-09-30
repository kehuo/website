# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-22 16:08:13
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-30 16:29:47

from flask import Flask, render_template
from app import ml
from app import werewolf

from .config import config


def create_app(config_name=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
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

    ml.init_app(app, '/ml')
    werewolf.init_app(app, '/werewolf')

    @app.route('/')
    def homepage():
        return render_template("index.html")

    return app
