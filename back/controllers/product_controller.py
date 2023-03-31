# back/controllers/product_controller.py

from flask import Blueprint, jsonify, request
from models.product import Product, db
from utils.validators import validate_product_data

bp = Blueprint('product', __name__, url_prefix='/api/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

@bp.route('/', methods=['POST'])
def create_product():
    validation_error = validate_product_data()
    if validation_error:
        return validation_error

    data = request.get_json()

    # Validez les données du nouveau produit
    if 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Créez le nouveau produit
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        image_url=data.get('image_url', ''),
        stock=data['stock']
    )

    db.session.add(product)
    db.session.commit()

    return jsonify(product.to_dict()), 201
