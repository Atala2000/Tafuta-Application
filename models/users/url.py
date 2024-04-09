#!/usr/bin/env python3
"""
Module that creates flask routes for users
"""
from flask import Blueprint, render_template, jsonify, request, make_response

from models.users import models
from models.users.database import DataStorage

data = DataStorage()

users = Blueprint("users", __name__, template_folder="templates", url_prefix="/users")


@users.route("/items", strict_slashes=False)
def items():
    """
    Returns a list of all items in the database
    """

    return jsonify({"Items": data.count(models.Items)})


@users.route("/items/<category>")
def category(category):
    """
    Returns a list of items in a given category
    """

    data = DataStorage()

    return jsonify({"Items": data.filter(models.Items, category=category)})


@users.route("/items/<int:id>")
def item(id):
    """
    Returns a single item
    """

    return jsonify({"Item": data.get(models.Items, id)})


@users.route("/items/connected")
def connected():
    """
    Returns a list of connected items
    """

    return jsonify({"Items": data.count(models.Connected_Items)})


@users.route("/items/connected/<int:id>")
def connected_item(id):
    """
    Returns a single connected item
    """

    return jsonify({"Item": data.get(models.Connected_Items, id)})


@users.route("/items/connected/<int:id>/owner")
def connected_owner(id):
    """
    Returns the owner of a connected item
    """

    return jsonify({"Owner": data.get(models.Users, id)})


@users.route("/items/connected/<int:id>/reporter")
def connected_reporter(id):
    """
    Returns the reporter of a connected item
    """

    return jsonify({"Reporter": data.get(models.Users, id)})


@users.route("/items/connected/<int:id>/location")
def connected_location(id):
    """
    Returns the location of a connected item
    """

    return jsonify({"Location": data.get(models.Connected_Items, id)})


@users.route("items", methods=["POST"])
def add_item():
    """
    Adds a new item to the database
    """
    data.add(
        models.Items(
            date_found=request.json["date_found"],
            location_found=request.json["location_found"],
            description=request.json["description"],
            filename=request.json["filename"],
            category=request.json["category"],
            users_id=request.json["users_id"],
        )
    )

    return make_response(jsonify({"message": "Item added"}), 201)


@users.route("/signup", method=['POST'])
def signup():
    """
    Adds a new user to the database
    """
    data.add(
        models.Users(
            username=request.json["username"],
            email=request.json["email"],
            password=request.json["password"],
        )
    )

    return make_response(jsonify({"message": "User added"}), 201)