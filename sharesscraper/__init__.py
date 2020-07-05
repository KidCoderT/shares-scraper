from flask import Flask

app = Flask(__name__)

from sharesscraper import views
