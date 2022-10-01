#Patients
#Id, Name, Last Name 1, Last Name 2, Genre, Weigth, Height, Age, Inscription Date, Last Date, Next Date

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class patients(db.Model):
    __tablename__ = "patients"
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    cel_number = db.Column(db.Integer)
    email = db.Column(db.String(200))
    gender = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    age = db.Column(db.Integer)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    dates = db.relationship('dates', backref='patient', lazy=True)