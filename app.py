from flask import Flask, render_template, url_for, request, jsonify
import os
import time


from werewolf.werewolf_module import werewolf_api
from ml.ml_module import ml_api

import web_config

app = Flask(__name__)
app.config['DEBUG'] = web_config.DEBUG
app.register_blueprint(werewolf_api, url_prefix='/werewolf')
app.register_blueprint(ml_api,url_prefix='/ml')


@app.route('/')
def homepage():
    return render_template("index.html")




if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response



if __name__ == '__main__':
    app.run(debug=web_config.DEBUG, port=web_config.PORT)
    #app.run(debug=True, port=5003)
    #app.run(debug=True)
