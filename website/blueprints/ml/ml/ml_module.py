# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-19 17:53:51
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-22 19:02:24
from flask import Blueprint, render_template, request, url_for

from ml.predictor import predict
from ml.markdown import get_md_dir

ml_api = Blueprint('ml_api', __name__, template_folder='templates', static_folder='static')


@ml_api.route('/')
def home():
    with open(get_md_dir() / 'ml.md') as f:
        content = f.read()
    return render_template("ml.html", content=content)


@ml_api.route('/mnist-canvas', methods=['GET', 'POST'])
def mnist_canvas():
    if request.method == 'POST':
        image = request.files['predictImg']
        # filename = str(int(time.mktime(time.localtime()))) + '.png'
        # imgurl = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # predictImg.save(imgurl)
        results, probabilities = predict('mnist', [image])
        return str(results[0])
    else:
        return render_template("mnist-canvas.html")


@ml_api.route('/project')
def project():
    project_name = request.args.get('name')
    with open(get_md_dir() / (project_name + '.md')) as f:
        content = f.read()
    return render_template("project.html", content=content, project_name=project_name)
