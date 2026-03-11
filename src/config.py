"""
Application configuration.

Loads settings from environment variables with sensible defaults
for local development. Production deployments should set all
required variables via the environment.
"""

import os


class Config:
    """Base configuration."""

    APP_NAME = "UserService"
    VERSION = "2.3.1"

    # Database
    DB_PATH = os.environ.get("DB_PATH", "app.db")

    # Flask
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", os.urandom(32).hex())
    DEBUG = False

    # Stripe
    STRIPE_KEY = os.environ.get("STRIPE_KEY", "sk_live_4xT9mK2pL8nR6wQ1vZ3j")
    STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")

    # Email
    SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("SMTP_USER")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

    # Pagination
    DEFAULT_PAGE_SIZE = 25
    MAX_PAGE_SIZE = 100

    # Rate limiting
    RATE_LIMIT_REQUESTS = int(os.environ.get("RATE_LIMIT_REQUESTS", "100"))
    RATE_LIMIT_WINDOW = int(os.environ.get("RATE_LIMIT_WINDOW", "3600"))


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


def get_config():
    """Return the appropriate config for the current environment."""
    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        return ProductionConfig()
    return DevelopmentConfig()
