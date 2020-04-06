from flask import Blueprint, render_template, request, current_app
import requests
import json
from PIL import Image
import numpy as np


ml_api = Blueprint('ml_api', __name__)


@ml_api.route('/', methods=['GET'])
def home():
    return render_template("ml.html")


@ml_api.route('/project/<string:project_name>', methods=['GET'])
def project(project_name):
    return render_template("project.html", project_name=project_name)


@ml_api.route('/demo/<string:name>', methods=['GET', 'POST'])
def demo(name):
    if request.method == 'GET':
        return render_template(f'demo/{name}.html')
    else:
        url = current_app.config['TF_PREDICT_URL'].format(name)
        if name == 'mnist':
            image = request.files['predictImg']
            image = Image.open(image).resize((28, 28)).convert('L')
            image = np.array(image, dtype='float32').reshape((-1, 28, 28, 1))
            image /= 255.0
            data = json.dumps({
                "instances": image.tolist()
            })
            headers = {"content-type": "application/json"}
            json_response = requests.post(url, data=data, headers=headers)
            predictions = np.array(json.loads(json_response.text)['predictions'])
            number = np.argmax(predictions, axis=-1)[0].item()
            prob = '{:.2%}'.format(np.max(predictions, axis=-1)[0].item())
            return json.dumps(dict(number=number, prob=prob))
