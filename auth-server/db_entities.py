import mongoengine
from mongoengine import Document, StringField

class Users(Document):
    username = StringField(required=True, unique=True)
    password = StringFiled(required=True)
