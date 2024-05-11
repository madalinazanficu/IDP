import jwt
from flask import request, Response
from functools import wraps

# Secret key to sign JWT tokens
SECRET_KEY = "chupacabra"
CREDENTIALS_ERROR = "Invalid credentials"

# Function to generate JWT token
def generate_token(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

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

# # Validate token decorator
# def token_required(f):
#     def decorator(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return 'Token is missing', 401

#         try:
#             # Verify token
#             payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#             kwargs['token_payload'] = payload
#         except jwt.ExpiredSignatureError:
#             return 'Token is expired', 401
#         except jwt.InvalidTokenError:
#             return 'Invalid token', 401

#         return f(*args, **kwargs)

#     return decorator
