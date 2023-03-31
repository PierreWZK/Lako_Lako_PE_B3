# back/controllers/search.py

from flask import Blueprint, request, jsonify
from models.product import Product

bp = Blueprint('search_controller', __name__, url_prefix='/api/search')

@bp.route('/products', methods=['GET'])
def search_products():
    query = request.args.get('query', '')

    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    search_results = Product.query.filter(Product.name.ilike(f'%{query}%')).all()

    return jsonify([product.to_dict() for product in search_results])
