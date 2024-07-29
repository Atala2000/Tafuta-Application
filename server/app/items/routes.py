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
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from app.models import models
from app.models.database import DataStorage
from app.items import bp as items
from app.utils.africa_talks import send_sms
from flask_mail import Mail, Message

data = DataStorage()
mail = Mail()


@items.route("/notify-owner/<int:id>", methods=["POST"])
@jwt_required()
def notify_owner(id):
    # Fetch the item by ID
    item = data.get(models.Items, id)
    
    if item:
        # Fetch the user associated with the item
        user = data.get(models.Users, item.users_id)
        
        if user:
            # Construct the SMS message
            sms_message = f"Hello {user.first_name}, your lost item has been found. Please contact us at {user.email}."
            message = {
                "sms_message": sms_message,
                "phone_no": user.phone_no
            }
            
            # Send the SMS
            response = send_sms(message)
            
            return jsonify({"message": "Owner notified successfully", "response": response}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Item not found"}), 404



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
def get_all_items():
    """
    Returns a list of all items in the database with file URLs
    """
    items_list = data.all(models.Items)
    if items_list:
        items_data = data.to_dict(items_list)
        for item in items_data:
            item["file_url"] = url_for("items.get_item_file", filename=item["filename"])
        return jsonify(items_data)
    else:
        return jsonify({"error": "No items found"}), 404

@items.route("/add", methods=["POST"])
@jwt_required()
def add_item():
    current_app.logger.info("add_item called")
    current_app.logger.info(f"JWT identity: {get_jwt_identity()}")

    users_upload_folder = current_app.config["UPLOAD_FOLDER"]

    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"status": "error", "message": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(users_upload_folder, filename)
        try:
            file.save(file_path)

            user_email = get_jwt_identity()
            user = data.filter(models.Users, email=user_email)[0]
            new_item = models.Items(
                date_found=request.form["dateFound"],
                location_found=request.form["locationFound"],
                description=request.form["description"],
                filename=filename,
                category=request.form["category"],
                users_id=user.id,
            )
            data.add(new_item)

            file_url = url_for("items.get_item_file", filename=filename)
            return jsonify({"status": "success", "message": "Item added successfully", "file_url": file_url}), 201
        except Exception as e:
            current_app.logger.error(f"Error adding item: {e}")
            return jsonify({"status": "error", "message": f"An error occurred: {e}"}), 500
    else:
        return jsonify({"status": "error", "message": "File type not allowed"}), 400



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
    user = data.filter(models.Users, email=get_jwt_identity())[0]
    if item:
        item.date_found = request.form["date_found"]
        item.location_found = request.form["location_found"]
        item.description = request.form["description"]
        item.category = request.form["category"]
        item.users_id = user.id
        data.update()
        return jsonify({"message": "Item updated successfully"})
    else:
        return jsonify({"error": "Item not found"}), 404

@items.route("/category/<string:category>", methods=["GET"])
def get_items_by_category(category):
    """
    Returns a list of items by category with file URLs
    """
    items_list = data.filter(models.Items, category=category)
    if items_list:
        items_data = data.to_dict(items_list)
        for item in items_data:
            item["file_url"] = url_for("items.get_item_file", filename=item["filename"])
        return jsonify(items_data)
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

@items.route("/test", methods=["GET"])
@jwt_required()
def test_jwt():
    return jsonify({"message": "JWT is working!"})
