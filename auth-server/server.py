import mongoengine
import json
import os


from flask import Flask, request
from pymongo import MongoClient
from mongoengine import connect
from db_entities import Users


# Responses codes:
#     200 - OK
#     201 - Created
#     400 - Bad Request
#     404 - Not Found
#     409 - Conflict - NonUniqueError

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
database_connection = connect_to_database()
if database_connection is None:
    print("Exiting...")
    exit(1)
else:
    print("Connected to database!")



@app.route('/api//register', methods=['POST'])
def register():
    try:
        payload = request.get_json()
        username = payload['username']
        password = payload['password']

        try:
            user = Users(username=username, password=password)
            user.save()
            response = {
                "username": user.username,
                "password": user.password
            }
            return json.dumps(response), 201
        
        except mongoengine.errors.NotUniqueError as e:
            return '', 409
    
    except mongoengine.errors.NotUniqueError as e:
        return '', 400


@app.route('/api/users', methods=['GET'])
def getUsers():
    try:
        users = Users.objects
        response = []
        for user in users:
            response.append({
                "username" : user.username
            })
        return json.dumps(response), 200
        
    except mongoengine.errors.ValidationError as e:
        return '', 400


# ------------- Definire rute
@app.route('/')
def hello_world(): 
    return "Hello World!"


# ------------- Pornire server Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port=6000, debug=True)