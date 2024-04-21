import jwt
from flask import request

# Secret key to sign JWT tokens
SECRET_KEY = "chupacabra"
CREDENTIALS_ERROR = "Invalid credentials"

# Function to generate JWT token
def generate_token(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Validate token decorator
def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return 'Token is missing', 401

        try:
            # Verify token
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            kwargs['token_payload'] = payload
        except jwt.ExpiredSignatureError:
            return 'Token is expired', 401
        except jwt.InvalidTokenError:
            return 'Invalid token', 401

        return f(*args, **kwargs)

    return decorator
