from flask import Blueprint, flash, jsonify, redirect, request, url_for, current_app
import os
from werkzeug.utils import secure_filename

from models.users import models
from models.users.database import DataStorage

data = DataStorage()

users = Blueprint("users", __name__, template_folder="templates", url_prefix="/users")


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
