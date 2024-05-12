import jwt
from flask import request, Response
from functools import wraps

SECRET_KEY = "chupacabra"

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

# Function to extract token from authorization header
def extract_token():
    auth_header = request.headers.get('Authorization')
    
    if auth_header:
        token_array = auth_header.split(' ')  # Extract token from "Bearer token"
        if len(token_array) == 2:
            token = token_array[1]
        else:
            token = token_array[0]

        return token
    else:
        return None

# Function to validate and decode JWT token
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = extract_token()
        if not token:
            return Response(status=401)

        token_payload = decode_token(token)
        if not token_payload:
            return Response(status=401)

        kwargs['token_payload'] = token_payload
        return f(*args, **kwargs)

    return decorated_function
