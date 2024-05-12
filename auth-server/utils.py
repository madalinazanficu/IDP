import jwt

# Secret key to sign JWT tokens
SECRET_KEY = "chupacabra"
CREDENTIALS_ERROR = "Invalid credentials"

# Function to generate JWT token
def generate_token(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
