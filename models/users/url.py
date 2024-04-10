from flask import Blueprint, flash, jsonify, redirect, request, url_for, current_app
import os
from werkzeug.utils import secure_filename

from models.users import models
from models.users.database import DataStorage

data = DataStorage()

users = Blueprint("users", __name__, template_folder="templates", url_prefix="/users")

def allowed_file(filename):
    """
    Checks if the file is allowed
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config['USERS_ALLOWED_EXTENSIONS']

@users.route("/items", strict_slashes=False)
def items():
    """
    Returns a list of all items in the database
    """
    return jsonify({"Items": data.count(models.Items)})

@users.route("/items", methods=["POST"])
def add_item():
    """
    Adds a new item to the database
    """

    users_upload_folder = current_app.config['UPLOAD_FOLDER']
    users_allowed_extensions = current_app.config['USERS_ALLOWED_EXTENSIONS']


    try:
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

        if "file" not in request.files:
            flash("No file part")
            return jsonify({"error": "No file part"}), 400
        file = request.files["file"]
        if file.filename == '':
            flash("No selected file")
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename, users_allowed_extensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(users_upload_folder, filename))
            return jsonify({"message": "Item added"}), 201
        else:
            return jsonify({"error": "File type not allowed"}), 400
    except:
        return jsonify({"error": "An error occurred"}), 500

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
