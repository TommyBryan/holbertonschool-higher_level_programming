from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

app = Flask(__name__)

users = {
    "user1": generate_password_hash ("password1"),
    "user2": generate_password_hash("password2")
}

@auth.verify_password
def verify_password(username, password):
    user
