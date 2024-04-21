import mongoengine
from mongoengine import Document, StringField, SequenceField, FloatField, CASCADE, ReferenceField, IntField


class Categories(Document):
    _id = SequenceField(primary_key=True)
    name = StringField(required=True, unique=True)

class Products(Document):
    _id = SequenceField(primary_key=True)
    product = StringField(required=True)
    price = FloatField(required=True)
    quantity = IntField(required=True)
    description = StringField(required=True)
    category = ReferenceField(Categories, reverse_delete_rule=CASCADE)
    username = StringField(required=True)

