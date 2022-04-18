from email.policy import default
from flask import render_template, redirect, request, session
from fashlance import app
from fashlance.utils import *


@app.route('/')
def index():
    countries = all_nations()
    countries = [item for item in countries['name']]
    return render_template('index.html', countries=countries)

@app.route('/technologies', methods=['GET', 'POST'])
def technologies():
        name = session.get("keyword", None)
      #  print(name)
        countries = all_nations()
        for x, y in zip(countries['id'], countries['name']):
            df, _ = get_data(x)
                
        return render_template('technologies.html', year=df['year'].tolist(), val=df['values'].tolist())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    name = request.form.get('name')
    print(name)
    session["keyword"] = name
    countries = all_nations()
    for x, y in zip(countries['id'], countries['name']):
            if y == name:
                _, get_title = get_data(x)

    return render_template('dashboard.html', titles=get_title)


    




