from flask import render_template, redirect, request, session
from fashlance import app, db
from fashlance.models import Countries, Indicators
from fashlance.utils import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        nations = all_nations()
        nations = [dict(v) for _, v in nations.iterrows()]
        for item in nations:
            isExisting = db.session.query(Countries).filter(Countries.id == str(item["id"])).first()

            if isExisting:
                pass
            else:
                countries2database = Countries(
                    id=item['id'],
                    name=item['name'],
                    capitalCity=item['capitalCity'],
                    longitude=item['longitude'],
                    latitude=item['latitude']
            )
                db.session.add(countries2database)

        db.session.commit()

        list_countries = [value[0] for value in db.session.query(Countries.name)]


        return render_template('index.html', countries=list_countries)



@app.route('/technologies', methods=['GET', 'POST'])
def technologies():
    return render_template('technologies.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form.get('keyword')
        nation_info = db.session.query(Countries).filter(Countries.name == name).first()
        indicators=get_indicators()

        title = []

        for values in indicators:
            data = wbdata.get_data(values, country=nation_info.id)
            my_dict = data[0]
            values_view = my_dict.values()
            value_iterator = iter(values_view)
            first_value = next(value_iterator)
            title.append(first_value['value'])

        print(title)

        return render_template('dashboard.html', nation_info=nation_info, title=title)
    