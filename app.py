from flask import Flask
from models.users.url import models
from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "7948b0fc-ac48-4988-bda9-78cf1bd07f54"

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token =request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing'})

app.register_blueprint(models)


@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return "Logged in currently", 200

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=120))
        },
        app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authrnification Failed "'})


if __name__ == "__main__":
    app.run(host="localhost", port=3300, debug=True)
