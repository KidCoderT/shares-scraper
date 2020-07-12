from flask import Flask

app = Flask(__name__)
app.config.update(
    SECRET_KEY=b"asfsdft76rtdjghfy4uiut?/dl][fhfvnu6rgh",
)

from app import views
