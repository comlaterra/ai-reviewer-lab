"""
Authentication and authorization middleware.

Provides decorators for Bearer-token authentication and
role-based access control. Apply to any route that requires
a logged-in user.
"""

import functools

from flask import request, jsonify, g

from .models import get_db


def require_auth(f):
    """Verify the Bearer token and attach the user to the request context."""
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authentication required"}), 401

        token = auth_header.split(" ", 1)[1]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, role FROM users WHERE api_token = ?",
            (token,),
        )
        user = cursor.fetchone()
        conn.close()

        if not user:
            return jsonify({"error": "Invalid token"}), 401

        g.current_user = {"id": user[0], "username": user[1], "role": user[2]}
        return f(*args, **kwargs)
    return decorated


def require_role(role):
    """Check that the authenticated user has the specified role."""
    def decorator(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            if not hasattr(g, "current_user"):
                return jsonify({"error": "Authentication required"}), 401
            if g.current_user["role"] != role:
                return jsonify({"error": "Insufficient permissions"}), 403
            return f(*args, **kwargs)
        return decorated
    return decorator
