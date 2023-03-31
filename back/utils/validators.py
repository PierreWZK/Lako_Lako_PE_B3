# app/validators.py

from flask import jsonify, request

def validate_user_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    return None

def validate_product_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or not price:
        return jsonify({"error": "Missing required fields"}), 400

    return None
