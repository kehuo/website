import os
import logging
from flask import Flask, render_template
from website.config import config
from website.ml_module import ml_api
from website.markdown import init_md


def init_app(app):
    init_md(app)


def create_app(config_name=None):
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

    if app.config["GUNICORN"]:
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    app.register_blueprint(ml_api, url_prefix='/ml')
    init_app(app)

    @app.route('/')
    def homepage():
        return render_template('index.html')

    return app
