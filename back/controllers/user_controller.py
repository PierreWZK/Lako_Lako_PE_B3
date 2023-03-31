# back/controllers/user_controller.py

from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db
from utils.validators import validate_user_data

bp = Blueprint('user_controller', __name__, url_prefix='/api/users')

@bp.route('/', methods=['POST'])
def create_user():
    validation_error = validate_user_data()
    if validation_error:
        return validation_error

    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    existing_user = User.query.filter(User.email == email).first()
    if existing_user:
        return jsonify({'error': 'Email already in use'}), 409

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user': user.id}), 201

@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
