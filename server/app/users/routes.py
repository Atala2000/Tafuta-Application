from flask import jsonify, request
from app.models import models
from app.models.database import DataStorage
from app.users import bp as users

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


@users.route("/signup", methods=["POST"])
def signup():
    """
    Adds a new user to the database
    """
    try:
        data.add(
            models.Users(
                username=request.json["username"],
                email=request.json["email"],
                password=request.json["password"],
            )
        )

        return jsonify({"message": "User added"}), 201
    except:
        return jsonify({"error": "An error occurred"}), 500
