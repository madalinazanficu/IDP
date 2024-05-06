from flask import Flask, request, Response, jsonify
import requests
import jwt
from utils import SECRET_KEY, token_required

# ------------- Define Flask application
app = Flask(__name__)

# ------------- Utility functions
def getRequestBody():
    return request.get_json(silent=True)

def getRequestBodyParam(param):
    return request.args.get(param)

def createProductRequest(name, price, quantity, description, category_id, username):
    return {
        'name': name,
        'price': price,
        'quantity': quantity,
        'description': description,
        'category_id': category_id,
        'username': username
        }

def getOrCreateCategory(category):
    # Call io-service endpoint to create or assign category
    response = requests.get('http://host.docker.internal:5001/io/categories')
    categories = response.json()
    category_exists = False
    category_id = None
    for c in categories:
        if c['name'].lower() == category.lower():
            category_exists = True
            category_id = c['id']
            break
    if not category_exists:
        response = requests.post('http://host.docker.internal:5001/io/category', json={'name': category})
        category_id = response.json()['id']
    
    return category_id

# ------------- Post a new product
@app.route('/business/product', methods=['POST'])
@token_required
def add_product(token_payload):
    # Only allow sellers to add products
    if token_payload.get('type') != 'seller':
        return Response(status=403)
    
    # Extract payload
    payload = getRequestBody()

    if not payload:
        return Response(status=400)
    
    # Extract data from payload
    name = payload.get('name')
    price = payload.get('price')
    quantity = payload.get('quantity')
    description = payload.get('description')
    category = payload.get('category')

    # Check if all required fields are present
    if not name or not price or not quantity or not description:
        return Response(status=400)
    else:
        # Convert to correct data types
        try:
            price = float(price)
            quantity = int(quantity)
        except:
            return Response(status=400)
        
        # Check if fields are valid
        if price < 0 or quantity < 0:
            return Response(status=400)
        
        # Check if category is present or assign default
        if not category:
            category = 'Others'
    
    category_id = getOrCreateCategory(category)

    # Call io-service endpoint to create product
    username = token_payload.get('username')
    payload = createProductRequest(name, price, quantity, description, category_id, username)
    
    response = requests.post('http://host.docker.internal:5001/io/product', json=payload)
    
    return Response(status=response.status_code)

# ------------- Start Flask server
if __name__ == '__main__':
    app.run('0.0.0.0', port=4001, debug=True)