from flask import render_template
from sharesscraper import app
from sharesscraper.data import my_table_data


@app.route('/')
def hello_world():
    return render_template('home.html', table_data=my_table_data, number=len(my_table_data))

