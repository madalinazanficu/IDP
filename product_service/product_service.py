from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/products_db'
mongo = PyMongo(app)

@app.route('/products', methods=['GET'])
def get_products():
    products = mongo.db.products.find()
    return jsonify({'products': [product for product in products]})

if __name__ == '__main__':
    app.run(debug=True)