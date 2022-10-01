# Ingredients
# name, amount, unit, 
# imagen

# caloricBreakdown - Desglose de calorías
## percentProtein - porcentaje de proteína
## percentFat - porcentaje de grasa
## percentCarbs - porcentaje de carbohidratos

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ingredients(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(30), nullable=False)
    imagen_url = db.Column(db.String)
    percentProtein = db.Column(db.Float, nullable=False)
    percentFat = db.Column(db.Float, nullable=False)
    percentCarbs = db.Column(db.Float, nullable=False)

    def __init__(self, name, amount, unit, imagen_url, percentProtein, percentFat, percentCarbs):
        super().__init__()
        self.name = name
        self.amount = amount 
        self.unit = unit
        self.imagen_url = imagen_url
        self.percentProtein = percentProtein
        self.percentFat = percentFat
        self.percentCarbs = percentCarbs

    def serialize(self): # To JSON, dict
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.description,
            "unit": self.creation_date,
            "imagen_url": self.modification_date,
            "caloricBreakdown": [{
                "percentProtein": self.percentProtein,
                "percentFat": self.percentProtein,
                "percentCarbs": self.percentProtein,
            }]
        }