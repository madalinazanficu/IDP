import mongoengine
from mongoengine import Document, StringField, FloatField

class Product(Document):
    product = StringField(required=True, unique=True)
    price = FloatField(required=True)
