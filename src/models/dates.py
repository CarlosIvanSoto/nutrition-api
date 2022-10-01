from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class dates(db.Model):
    __tablename__ = "dates"
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)