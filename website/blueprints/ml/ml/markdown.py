from flask_misaka import Misaka
from pathlib import Path

md = Misaka(footnotes=True)


def init_md(app):
    md.init_app(app)
