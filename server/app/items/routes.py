from flask import (
    Blueprint,
    jsonify,
    logging,
    request,
    current_app,
    send_from_directory,
    url_for,
    render_template
)
import os
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
from app.models import models
from app.models.database import DataStorage
from app.items import bp as items

data = DataStorage()


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


@jwt_required()
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
            file_url = url_for("items.get_item_file", filename=filename)
            return (
                jsonify({"message": "Item added successfully", "file_url": file_url}),
                201,
            )
        except Exception as e:
            return jsonify({"error": f"An error occurred: {e}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400


@items.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_item(id):
    """
    Returns a single item from the database
    """
    item = data.get(models.Items, id)
    if item:
        item_details = data.to_dict(item)
        file_url = url_for("items.get_item_file", filename=item.filename)
        item_details["file_url"] = file_url
        return jsonify(item_details)
    else:
        return jsonify({"error": "Item not found"}), 404


@items.route("/uploads/<filename>")
def get_item_file(filename):
    """
    Returns the file associated with a single item from the database.
    """
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        filename,
        as_attachment=False,
    )


@items.route("/<int:id>", methods=["DELETE"])
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


@jwt_required()
@items.route("/<int:id>", methods=["PUT"])
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


@items.route("/category/<string:category>", methods=["GET"])
def get_items_by_category(category):
    """
    Returns a list of items by category
    """
    items_list = data.filter(models.Items, category=category)
    if items_list:
        return jsonify(data.to_dict(items_list))
    else:
        return jsonify({"error": "No items found"}), 404


@items.route("/user/<int:users_id>", methods=["GET"])
def get_items_by_user(users_id):
    """
    Returns a list of items by user
    """
    items_list = data.filter(models.Items, users_id=users_id)
    if items_list:
        return jsonify(data.to_dict(items_list))
    else:
        return jsonify({"error": "No items found"}), 404


@items.route("/item/test/<int:id>", methods=["GET"], strict_slashes=False)
def display_item(id):
    """
    Renders the item details along with the uploaded image.
    """
    item = data.get(models.Items, id)
    if item:
        item_details = data.to_dict(item)
        file_url = url_for("items.get_item_file", filename=item.filename)
        item_details["file_url"] = file_url
        return render_template("item.html", item=item_details)
    else:
        return jsonify({"error": "Item not found"}), 404
