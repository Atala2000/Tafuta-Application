from flask_jwt_extended import create_access_token
from app.auth import bp as auth
from flask import request, jsonify
from app.models.models import Users
from app.models.database import DataStorage
import bcrypt


@auth.route("/login", methods=["POST"], strict_slashes=False)
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    data_storage = DataStorage()  # Instantiate DataStorage class
    user = data_storage.filter(Users, email=email)[0] # Retrieve the user object

    if not user:
        return jsonify({"message": "User does not exist"}), 401

    hashed_password = user.password.encode("utf-8")
    password_bytes = password.encode("utf-8")

    if bcrypt.checkpw(password_bytes, hashed_password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"Error": "Authentication error, wrong password"}), 401

