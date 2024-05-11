from flask import request

def partial_match(keyname, product_name):
    for n in product_name.split():
        if set(keyname.lower()).issubset(set(n.lower())) and len(n) - len(keyname) <= 1:
            return True
        if set(n.lower()).issubset(set(keyname.lower())) and len(keyname) - len(n) <= 1:
            return True
    return False

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