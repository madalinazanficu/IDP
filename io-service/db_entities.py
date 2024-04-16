import mongoengine
from mongoengine import Document, StringField, FloatField

class Products(Document):
    product = StringField(required=True, unique=True)
    price = StringField(required=True)
