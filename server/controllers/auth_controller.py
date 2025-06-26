from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {"error": "Username and password required"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print("Login data received:", data)

    user = User.query.filter_by(username=username).first()
    print("User found:", user)

    if user and user.check_password(password):
        print("Password is correct")
        token = create_access_token(identity=str(user.id))
        return {"access_token": token}, 200

    print("Invalid credentials")
    return {"error": "Invalid credentials"}, 401