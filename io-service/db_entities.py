import mongoengine
from mongoengine import Document, StringField, SequenceField, FloatField, CASCADE, ReferenceField


class Categories(Document):
    _id = SequenceField(primary_key=True)
    name = StringField(equired=True, unique=True)

class Products(Document):
    _id = SequenceField(primary_key=True)
    product = StringField(required=True, unique=True)
    price = FloatField(required=True)
    quantity = FloatField(required=True)
    description = StringField(required=True)

