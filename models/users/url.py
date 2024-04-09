#!/usr/bin/env python3
"""
Module that creates flask routes for users
"""
from flask import Blueprint, render_template, jsonify, request, make_response

models = Blueprint("models", __name__, template_folder="templates", url_prefix="/users")


@models.route("/items", strict_slashes=False)
def items():
    """
    Returns a list of all items in the database
    """
    import models
    import database

    # result = session.query(models.Users).all()
    return {
        "total results": "result",
    }, 200
