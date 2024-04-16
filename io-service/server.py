import mongoengine
import json
import os


# Responses codes:
#     200 - OK
#     201 - Created
#     400 - Bad Request
#     404 - Not Found
#     409 - Conflict - NonUniqueError


from flask import Flask, request
from pymongo import MongoClient
from mongoengine import connect
from db_entities import Product

# ------------- Definire aplicatie Flask
app = Flask(__name__)

# ------------- Definire rute
@app.route('/')
def hello_world(): 
    return "Hello World from IO/SERVICE!"


# ------------- Pornire server Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)