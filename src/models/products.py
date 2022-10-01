# Products
# marca, titulo, precio
# porcion
# imagen_url / 2
# txt_ingredientes
# num_ingredients

# brand, title, price, serving_size, img_url, nutri_decl_url, txt_ingredients, num_ingredients

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    title = db.Column(db.String)
    price = db.Column(db.Float)
    serving_size = db.Column(db.String)
    images_urls = db.Column(db.String)
    txt_ingredients = db.Column(db.String)
    num_ingredients = db.Column(db.Integer)

                                                        # [2, 3, 4, 5]
    def __init__(self, title, brand, price, serving_size, images_urls, txt_ingredients, num_ingredients):
        super().__init__()
        self.title = title
        self.brand = brand
        self.price = price
        self.serving_size = serving_size
        self.images_urls = str(images_urls)
        self.txt_ingredients = txt_ingredients
        self.num_ingredients = num_ingredients


    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "brand": self.brand,
            "price": self.price,
            "serving_size": self.serving_size,
            "images": self.images_urls,
            "ingredients": {
                "count": self.num_ingredients,
                "text": self.txt_ingredients
            }
        }