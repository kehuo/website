from flask_misaka import Misaka

md = Misaka(footnotes=True)


def init_md(app):
    md.init_app(app)
