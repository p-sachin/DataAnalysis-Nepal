from fashlance import db 
from fashlance import app
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

@app.before_first_request
def create_tables():
    db.create_all()

class CountryData(db.Model):
    id = db.Column(db.String(10),primary_key=True,nullable=False)
    title = db.Column(db.String(255),nullable=False)
    indicator = db.Column(db.String(255),nullable=False)
    year = db.Column(MutableList.as_mutable(PickleType), default=[])
    values =  db.Column(MutableList.as_mutable(PickleType), default=[])