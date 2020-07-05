from flask import render_template
from sharesscraper import app
from sharesscraper.data import *


@app.route('/')
def hello_world():
    return render_template('home.html')

