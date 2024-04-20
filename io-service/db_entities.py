import mongoengine
from mongoengine import Document, StringField, SequenceField, FloatField, CASCADE, ReferenceField


class Categories(Document):
    name = StringField(primary_key=True)

class Products(Document):
    _id = SequenceField(primary_key=True)
    category = ReferenceField(Categories, required=True, reverse_delete_rule=CASCADE)
    
    product = StringField(required=True)
    price = FloatField(required=True)
    quantity = FloatField(required=True)
    description = StringField(required=True)

