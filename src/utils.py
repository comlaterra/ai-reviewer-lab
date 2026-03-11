"""
Shared utility functions.

Validators, formatters, and helpers used across the application.
"""

import re
import logging

logger = logging.getLogger(__name__)


def validate_email(email):
    """Basic email format validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_username(username):
    """Username must be 3-30 alphanumeric characters or underscores."""
    if not username or not isinstance(username, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9_]{3,30}$", username))


def sanitize_user_response(user_row):
    """Strip sensitive fields before returning user data to the client."""
    if user_row is None:
        return None
    return {
        "id": user_row["id"],
        "username": user_row["username"],
        "email": user_row["email"],
        "role": user_row["role"],
        "plan": user_row["plan"],
        "credits": user_row["credits"],
        "created_at": user_row["created_at"],
    }


def paginate_query(cursor, query, params=(), page=1, per_page=25):
    """Add LIMIT/OFFSET pagination to a query."""
    offset = (page - 1) * per_page
    paginated = f"{query} LIMIT ? OFFSET ?"
    cursor.execute(paginated, (*params, per_page, offset))
    return cursor.fetchall()
