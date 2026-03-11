"""
User management endpoints.

Handles registration, profile lookup, account deletion,
and admin user listing.
"""

from flask import Blueprint, request, jsonify

from ..services.users import get_user, create_user, delete_user, list_users
from ..auth import require_auth, require_role
from ..utils import validate_email, validate_username

users_bp = Blueprint("users", __name__)


@users_bp.route("/user/<user_id>", methods=["GET"])
@require_auth
def fetch_user(user_id):
    """Fetch a single user by ID."""
    try:
        user = get_user(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@users_bp.route("/user", methods=["POST"])
def register():
    """Register a new user account. Public endpoint."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email, and password are required"}), 400

    if not validate_username(username):
        return jsonify({"error": "Invalid username format"}), 400

    if not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    result = create_user(
        username=username,
        email=email,
        password=password,
        role=data.get("role", "user"),
        plan=data.get("plan", "free"),
        referral_code=data.get("referral_code"),
    )
    return jsonify(result), 201


@users_bp.route("/user/<user_id>", methods=["DELETE"])
@require_auth
def remove_user(user_id):
    """Delete a user account."""
    delete_user(user_id)
    return jsonify({"status": "deleted"})


@users_bp.route("/admin/users", methods=["GET"])
def list_all_users():
    """List all users. Admin only."""
    users = list_users()
    return jsonify(users)
