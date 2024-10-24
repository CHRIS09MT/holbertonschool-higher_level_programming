from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    return jsonify(users)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    
    user = users.get(username)
    
    if user:
        return jsonify(users)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def new_user():
    
    user_add = request.get_json()
    username = user_add.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_add
    return jsonify({"message": "User added", "user": user_add}), 201
    

if __name__ == "__main__":
    app.run()