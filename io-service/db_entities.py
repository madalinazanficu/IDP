import mongoengine
from mongoengine import Document, StringField, SequenceField, FloatField

class Products(Document):
    _id = SequenceField(primary_key=True)
    product = StringField(required=True)
    price = FloatField(required=True)
    category = StringField(required=True)