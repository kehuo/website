from flask import Blueprint, render_template, request, abort


ml_api = Blueprint('ml_api', __name__)


@ml_api.route('/')
def home():
    return render_template("ml.html")


@ml_api.route('/project')
def project():
    project_name = request.args.get('name')
    return render_template("project.html", project_name=project_name)


@ml_api.route('/demo')
def demo():
    abort(404)
