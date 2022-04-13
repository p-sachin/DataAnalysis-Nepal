from flask import render_template, redirect, request
from fashlance import app, db
from fashlance.utils import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/technologies')
def technologies():
    df = get_data('SP.POP.TOTL', 'IND')
    return render_template('technologies.html', year=df['year'].tolist(), val=df['values'].tolist())


