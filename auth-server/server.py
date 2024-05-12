import mongoengine
import json
import os

from flask import Flask, request, jsonify
from pymongo import MongoClient
from mongoengine import connect
from db_entities import Users
from utils import generate_token, CREDENTIALS_ERROR


# Responses codes:
#     200 - OK
#     201 - Created
#     400 - Bad Request
#     404 - Not Found
#     409 - Conflict - NonUniqueError

def connect_to_database():
    try:
        client = MongoClient(host=os.getenv('DB_HOSTNAME', 'mongo'),
                             port=int(os.getenv('DB_PORT', 27017)),
                             username=os.getenv('USERNAME_DB', 'admin'),
                             password=os.getenv('PASSWORD_DB', 'admin'),
                             authSource='admin')

        db_name = os.getenv('DB_NAME', 'clients_db')
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
database_connection = connect_to_database()
if database_connection is None:
    print("Exiting...")
    exit(1)
else:
    print("Connected to database!")


def usersSerializer(user):
    return {
        "username": user.username,
        "password": "*" * len(user.password),
        "type": user.type
    }


# ------------- Register endpoint
@app.route('/auth/register', methods=['POST'])
def register():
    try:
        payload = request.get_json()
        username = payload['username']
        password = payload['password']
        type = payload['type']

        try:
            user = Users(username=username, password=password, type=type)
            user.save()

            # Generate JWT token
            token = generate_token({'username': username, 'type': type})

            response = {
                "username": user.username,
                "password": user.password,
                "type": user.type,
                "token": token
            }
            return json.dumps(response), 201
        
        except mongoengine.errors.NotUniqueError as e:
            return '', 409
    
    except mongoengine.errors.NotUniqueError as e:
        return '', 400

# ------------- Login endpoint
@app.route('/auth/login', methods=['POST'])
def login():
    try:
        payload = request.get_json()
        username = payload['username']
        password = payload['password']

        user = Users.objects(username=username).first()
        if user is None:
            return CREDENTIALS_ERROR, 404

        if user.password == password:
            # Generate JWT token
            token = generate_token({'username': username, 'type': user.type})

            return jsonify({'token': token}), 200
        else:
            return CREDENTIALS_ERROR, 401

    except mongoengine.errors.ValidationError as e:
        return '', 400


@app.route('/auth/user/<username>', methods=['GET'])
def getUser(username):
    user = Users.objects(username=username).first()
    if user is None:
        return 'Not found', 404

    return json.dumps(user, default=usersSerializer), 200



# For debugging purposes
@app.route('/auth/users', methods=['GET'])
def getUsers():
    return json.dumps(list(Users.objects.all()), default=usersSerializer), 200


# For debugging purposes
@app.route('/auth/remove', methods=['DELETE'])
def delete_users():
    try:
        Users.objects.delete()
        return '', 200
    except mongoengine.errors.ValidationError as e:
        return '', 400


# ------------- Definire rute
@app.route('/')
def hello_world(): 
    return "Hello World!"


# ------------- Pornire server Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port=6001, debug=True)