from flask import Blueprint, flash, jsonify, redirect, request, url_for, current_app, render_template
import os
from werkzeug.utils import secure_filename

from models.users import models
from models.users.database import DataStorage

data = DataStorage()

items = Blueprint("items", __name__, template_folder="templates", url_prefix="/items")


def allowed_file(filename):
    """
    Checks if the file is allowed
    """
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["USERS_ALLOWED_EXTENSIONS"]
    )


@items.route("/", strict_slashes=False)
def items_count():
    """
    Returns a list of all items in the database
    """
    return jsonify({"Items": data.count(models.Items)})


@items.route("/add", methods=["POST"])
def add_item():
    users_upload_folder = current_app.config["UPLOAD_FOLDER"]

    # Check if a file is included in the request
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Validate file extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(users_upload_folder, filename))

        try:
            data.add(
                models.Items(
                    date_found=request.form["date_found"],
                    location_found=request.form["location_found"],
                    description=request.form["description"],
                    filename=filename,
                    category=request.form["category"],
                    users_id=request.form["users_id"],
                )
            )
            return jsonify({"message": "Item added successfully"}), 201
        except Exception as e:
            return jsonify({"error": f"An error occurred: {e}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400



@items.route("/items/<int:id>", methods=["GET"])
def get_item(id):
    """
    Returns a single item from the database
    """
    item = data.get(models.Items, id)
    if item:
        return jsonify(data.to_dict(item))
    else:
        return jsonify({"error": "Item not found"}), 404
    
@items.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    """
    Deletes an item from the database
    """
    item = data.get(models.Items, id)
    if item:
        data.delete(item)
        return jsonify({"message": "Item deleted successfully"})
    else:
        return jsonify({"error": "Item not found"}), 404


@items.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    """
    Updates an item in the database
    """
    item = data.get(models.Items, id)
    if item:
        item.date_found = request.form["date_found"]
        item.location_found = request.form["location_found"]
        item.description = request.form["description"]
        item.category = request.form["category"]
        item.users_id = request.form["users_id"]
        data.update()
        return jsonify({"message": "Item updated successfully"})
    else:
        return jsonify({"error": "Item not found"}), 404
    

@items.route("/items/<string:category>", methods=['GET'])
def get_items_by_category(category):
    """
    Returns a list of items by category
    """
    items = data.filter(models.Items, category=category)
    if items:
        return jsonify(data.to_dict(items))
    else:
        return jsonify({"error": "No items found"}), 404

@items.route("/items/<int:users_id>")
def get_items_by_user(users_id):
    """
    Returns a list of items by user
    """
    items = data.filter(models.Items, users_id=users_id)
    if items:
        return jsonify(data.to_dict(items))
    else:
        return jsonify({"error": "No items found"}), 404