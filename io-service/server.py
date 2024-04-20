import mongoengine
import json
import os


# Responses codes:
#     200 - OK
#     201 - Created
#     400 - Bad Request
#     404 - Not Found
#     409 - Conflict - NonUniqueError


from flask import Flask, request, Response, jsonify
from pymongo import MongoClient
from mongoengine import connect
from db_entities import Products

def connect_to_database():
    try:
        client = MongoClient(host=os.getenv('DB_HOSTNAME', 'mongo'),
                             port=int(os.getenv('DB_PORT', 27017)),
                             username=os.getenv('USERNAME_DB', 'admin'),
                             password=os.getenv('PASSWORD_DB', 'admin'),
                             authSource='admin')

        db_name = os.getenv('DB_NAME', 'products_db')
        db = client[db_name]

        connect(
            db=db_name,
            host=os.getenv('DB_HOSTNAME', 'mongo'),
            port=int(os.getenv('DB_PORT', 27017)),
            username=os.getenv('USERNAME_DB', 'admin'),
            password=os.getenv('PASSWORD_DB', 'admin'),
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
    print("Error connecting to database!")
    exit(1)
else:
    print("Connected to database!")

# ------------- Utility functions
def getRequestBody():
    return request.get_json(silent=True)

def getRequestBodyParam(param):
    return request.args.get(param)

def productSerializer(product):
    return {
        'id': int(product.id),
        'product': str(product.product),
        'price': float(product.price),
        'category': str(product.category)
    }

# ------------- Add new product endpoint
@app.route('/api/product', methods=['POST'])
def add_product():
    # Extract payload
    payload = getRequestBody()

    if not payload:
        return Response(status=400)
    
    # Extract data from payload
    name = payload.get('name')
    price = payload.get('price')
    category = payload.get('category')

    # Check if all required fields are present
    if not name or not price:
        return Response(status=400)
    else:
        try:
            price = float(price)
        except:
            return Response(status=400)
        
        if not category:
            category = 'Other'

    # Create new product
    product = Products(product=name, price=price, category=category)
    try:
        product.save()
    except mongoengine.errors.NotUniqueError:
        return Response(status=409)
    except:
        return Response(status=400)
    
    return jsonify({'id': product.pk}), 201
    

# ------------- Get all products endpoint
@app.route('/api/products', methods=['GET'])
def get_products():
    return json.dumps(list(Products.objects.all()), default=productSerializer), 200

# ------------- Definire rute
@app.route('/')
def hello_world(): 
    return "Hello World from IO/SERVICE!"


# ------------- Pornire server Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)