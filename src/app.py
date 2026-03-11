"""
Application factory and entry point.

Creates the Flask app, registers blueprints, and sets up
global error handlers.
"""

from flask import Flask

from .config import get_config
from .models import init_db


def create_app():
    """Create and configure the Flask application."""
    config = get_config()

    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize database on first request
    with app.app_context():
        init_db()

    # Register blueprints
    from .api.users import users_bp
    from .api.payments import payments_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(payments_bp, url_prefix="/billing")

    # Global error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Resource not found"}, 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return {"error": "Method not allowed"}, 405

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
