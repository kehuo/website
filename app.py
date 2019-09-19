from flask import Flask, render_template, url_for, request, jsonify
import os
import time


from werewolf.werewolf_module import werewolf_api
from ml.ml_module import ml_api

import config

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp'
app.register_blueprint(werewolf_api, url_prefix='/werewolf')
app.register_blueprint(ml_api,url_prefix='/ml')


@app.route('/')
def homepage():
    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=config.config_debug, port=config.config_port)
    #app.run(debug=True, port=5003)
