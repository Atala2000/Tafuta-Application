from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.auth import bp as auth
from app.models import models
from flask import request, jsonify
from app.models.models import Users
from app.models.database import DataStorage
import bcrypt

data_storage = DataStorage()

@auth.route("/login", methods=["POST"], strict_slashes=False)
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Instantiate DataStorage class
    user = data_storage.filter(Users, email=email)[0]  # Retrieve the user object

    if not user:
        return jsonify({"message": "User does not exist"}), 401

    hashed_password = user.password.encode("utf-8")
    password_bytes = password.encode("utf-8")

    if bcrypt.checkpw(password_bytes, hashed_password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"Error": "Authentication error, wrong password"}), 401


@auth.route("/signup", methods=["POST"], strict_slashes=False)
def signup():
    """
    Adds a new user to the database and logs them in
    """
    try:
        email = request.json.get("email")
        password = request.json.get("password")
        first_name = request.json.get("first_name")
        phone_no = request.json.get("phone_no")

        password_bytes = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        new_user = models.Users(
            email=email,
            password=hashed_password,
            first_name=first_name,
            phone_no=phone_no,
        )
        data_storage.add(new_user)

        # Automatically log in the user after signup
        access_token = create_access_token(identity=email)
        return jsonify(message="User added", access_token=access_token), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@auth.route("/user", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_user():
    user =  get_jwt_identity()
    return jsonify({"user": user})