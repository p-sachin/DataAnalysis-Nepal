from flask import render_template, redirect, request
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


@app.route('/tech/<indicator_id>', methods=['GET', 'POST'])
def tech(indicator_id):
    list_country=db.session.query(Indicators).filter(Indicators.indicator_id==indicator_id).first()
    year, values = get_data(list_country.indicator_id, list_country.country)

    return render_template('technologies.html', list_country=list_country, year=year, val=values)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form.get('keyword')
        nation_info = db.session.query(Countries).filter(Countries.name == name).first()
        abbr = nation_info.id
        ind_title = get_indicators(abbr)
        ind_title = [dict(v) for _, v in ind_title.iterrows()]
        print(ind_title)

        db.session.query(Indicators).delete()

        for item in ind_title:
            indicators2database = Indicators(
                indicator_id=item['indicator_id'],
                title=item['title'],
                country=item['country']
        )
            db.session.add(indicators2database)

        db.session.commit()

        list_sectors = db.session.query(Indicators).all()

        return render_template('dashboard.html', nation_info=nation_info, list_title=list_sectors)
    