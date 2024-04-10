from flask import Flask
from models.users.url import users
from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

# Load config file
app.config.from_pyfile("config.py") 


app.register_blueprint(users)



if __name__ == "__main__":
    app.run(host="localhost", port=3300, debug=True)
