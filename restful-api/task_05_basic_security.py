from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

# Base de datos de usuarios en memoria
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Verificación de usuario y contraseña
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# Ruta protegida con autenticación básica
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"msg": "Basic Auth: Access Granted"})

# Ruta para iniciar sesión y obtener un token JWT
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    if username in users and check_password_hash(users[username]["password"], password):
        role = users[username]["role"]
        access_token = create_access_token(identity={"username": username, "role": role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

# Ruta protegida con autenticación JWT
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"msg": "JWT Auth: Access Granted"})

# Ruta protegida solo para administradores
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"msg": "Admin Access: Granted"})

# Manejadores de errores personalizados de JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Ruta de inicio
@app.route("/")
@auth.login_required
def home():
    return "Hello, {}!".format(auth.current_user())

if __name__ == "__main__":
    app.run()
