from flask import render_template, redirect, request
from fashlance import app
from fashlance.utils import *


@app.route('/')
def index():
    countries = all_nations()
    countries = [item for item in countries['name']]
    return render_template('index.html', countries=countries)

@app.route('/technologies', methods=['GET', 'POST'])
def technologies():
    if request.method == 'POST':
        name = request.form.get('name')
        countries = all_nations()
        for x, y in zip(countries['id'], countries['name']):
            if y == name:
                df = get_data('SP.POP.TOTL', x)
                
        return render_template('technologies.html', year=df['year'].tolist(), val=df['values'].tolist())




