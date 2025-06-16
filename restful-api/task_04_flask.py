#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
""" In-memory user data """
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return str("Welcome to the Flask API!")

@app.route('/data')
def get_username():
    """ Return the user data as JSON """
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return (jsonify({"error": "User not found"}), 404)
    
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run()
