from flask import Flask, render_template, url_for, request, jsonify
import os
import time

import predict

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = 'tmp'


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/mnist', methods=['GET', 'POST'])
def mnist():
    if request.method == 'POST':
        predictImg = request.files['predictImg']
        # filename = str(int(time.mktime(time.localtime()))) + '.png'
        # imgurl = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # predictImg.save(imgurl)
        result, prob = predict.mnist_predict(predictImg)
        return str(result)
    else:
        return render_template("mnist.html")


if __name__ == '__main__':
    app.run()
