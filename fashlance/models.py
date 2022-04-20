from fashlance import db 
from fashlance import app
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

@app.before_first_request
def create_tables():
    db.create_all()


class Countries(db.Model):
    id = db.Column(db.String(10),primary_key=True,nullable=False)
    name = db.Column(db.String(255),nullable=False)
    capitalCity = db.Column(db.String(255),nullable=False)
    longitude = db.Column(db.DECIMAL(10,4))
    latitude = db.Column(db.DECIMAL(10,4))

class Indicators(db.Model):
    indicator_id = db.Column(db.String(128),primary_key=True,nullable=False)
