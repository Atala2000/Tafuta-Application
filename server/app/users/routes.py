from flask import jsonify, request
from flask_jwt_extended import jwt_required
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


@users.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_user(id: int) -> jsonify:
    """
    Deletes a user from the database
    Args:
        id (int): The id of the user to delete
    """
    user = data.get(models.Users, id)
    data.delete(user)
    return jsonify({"message": "User deleted"})

@jwt_required()
@users.route("/<int:id>", methods=["PUT"], strict_slashes=False)
def update_user(id: int) -> jsonify:
    """
    Updates a user in the database
    Args:
        id (int): The id of the user to update
    """
    try:
        user = data.get(models.Users, id)
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.email = request.form["email"]
        user.password = bcrypt.hashpw(request.form["password"].encode(), bcrypt.gensalt())
        user.phone_no = request.form["phone_no"]
        data.update()
        return jsonify({"message": "User updated"})
    except Exception as e:
        return jsonify({"message": f"An error occurred: {e}"})

