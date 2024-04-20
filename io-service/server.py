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
from db_entities import Products

def connect_to_database():
    try:
        client = MongoClient(host=os.environ['DB_NAME'],
                             port=27017,
                             username=os.environ['USERNAME_DB'],
                             password=os.environ['PASSWORD_DB'],
                             authSource='admin')

        db = client[os.environ['DB_NAME']]

        connect(
            db=os.environ['DB_NAME'],
            host=os.environ['DB_NAME'],
            username=os.environ['USERNAME_DB'],
            password=os.environ['PASSWORD_DB'],
            authentication_source='admin'
        )
        return db

    except:
        print("Error connecting to database!")
        return None

# ------------- Definire aplicatie Flask
app = Flask(__name__)


# ------------ Autentificare la baza de date
db = connect_to_database()
if db is None:
    print("Exiting...")
    exit(1)
else:
    print("Connected to database!")
    # db.create_collection('products')


# ------------- Add new product endpoint
@app.route('/api/product', methods=['POST'])
def add_product():
    try:
        payload = request.get_json()
        name = payload['name']
        price = payload['price']

        try:
            product = Products(name=name, price=price)
            product.save()
            response = {
                "name": product.name,
                "price": product.price
            }
            return json.dumps(response), 201
    
        except mongoengine.errors.NotUniqueError as e:
            return '', 409
    except:
        return '', 400
    

# ------------- Get all products endpoint
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Products.objects
        response = []
        for product in products:
            response.append(product.to_json())
        return json.dumps(response), 200

    except mongoengine.errors.ValidationError as e:
        return '', 400

# ------------- Definire rute
@app.route('/')
def hello_world(): 
    return "Hello World from IO/SERVICE!"


# ------------- Pornire server Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)