from flask import render_template
from app import app
from sharesscraper.data import *


@app.route('/')
def hello_world():
    return hello

