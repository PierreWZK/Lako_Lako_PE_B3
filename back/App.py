from flask import Flask, jsonify
from flask_cors import CORS
from config import DevelopmentConfig
from extensions import db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    with app.app_context():
        from models.product import Product
        from controllers import product_controller, user_controller, search, auth

        app.register_blueprint(product_controller.bp)
        app.register_blueprint(user_controller.bp)
        app.register_blueprint(search.bp)
        app.register_blueprint(auth.bp)
        
        db.create_all()

        @app.route('/')
        def index():
            return jsonify({"message": "Bienvenue sur l'API de notre plateforme e-commerce !"}), 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
