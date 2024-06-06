from flask import jsonify, request
from app.models import models
from app.models.database import DataStorage
from app.users import bp as users
import bcrypt

data = DataStorage()


@users.route("/", strict_slashes=False)
def user_list():
    """
    Returns a list of all users in the database
    """
    return jsonify({"Users": data.count(models.Users)})


@users.route("/<int:id>", methods=["GET"], strict_slashes=False)
def specific_user(id: int) -> jsonify:
    """
    Retrieves Details of a specific user using their id
    Args:
        id (int): The id of the user to retrieve
    """
    user = data.get(models.Users, id)
    return jsonify(data.to_dict(user))


@users.route("/signup", methods=["POST"], strict_slashes=False)
def signup():
    """
    Adds a new user to the database
    """
    try:

        password_bytes = request.json.get("password").encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        data.add(
            models.Users(
                email=request.json["email"],
                password=hashed_password,
                first_name=request.json.get("first_name"),
                phone_no=request.json.get("phone_no")
            )
        )

        return jsonify({"message": "User added"}), 201
    except Exception as e:
        return jsonify({"error": e}), 500
