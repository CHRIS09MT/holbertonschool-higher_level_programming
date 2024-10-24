from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    return jsonify(users)


@app.route("/status")
def status():
    return "OK"


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def new_user():
    
    data = request.get_json()
    
    username = data['username']
    name = data['name']
    age = data['age']
    city = data['city']
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    
    users[username] = {
        'name': name,
        'age': age,
        'city': city
    }
    
    return jsonify({
        'message': 'User added successfully',
        'user': users[username]
    }), 201
    

if __name__ == "__main__":
    app.run()