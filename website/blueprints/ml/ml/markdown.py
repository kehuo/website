from flask_misaka import Misaka
from pathlib import Path

md = Misaka()


def init_md(app):
    md.init_app(app)


def get_md_dir():
    return Path(__file__).resolve().parent / 'markdowns'
