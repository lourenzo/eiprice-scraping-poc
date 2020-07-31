from flask_mongoengine import MongoEngine

db = MongoEngine()

class ProductOffer(db.Document):
    ean = db.StringField()
    sku = db.StringField()
    name = db.StringField()
    department = db.StringField()
    category = db.StringField()
    subcategory = db.StringField()
    brand = db.StringField()
    attributes = db.DictField()
    in_stock = db.BooleanField()
    price = db.DecimalField()
    installments = db.IntField()
    installment_price = db.DecimalField()
    interest_rate = db.DecimalField()
    url = db.URLField()
    image = db.URLField()
