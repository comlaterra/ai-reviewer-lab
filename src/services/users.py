"""
User management service.

Handles CRUD operations, referral credit system,
and welcome email notifications.
"""

from ..models import get_db
from ..utils import sanitize_user_response


def get_user(user_id):
    """Fetch a single user by ID."""
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return sanitize_user_response(row)


def create_user(username, email, password, role="user", plan="free", referral_code=None):
    """
    Register a new user account.

    If a referral_code is provided, the referring user receives
    10 credits after successful registration.
    """
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO users (username, email, password, role, plan, referral_code)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (username, email, password, role, plan, referral_code),
    )
    conn.commit()
    user_id = cursor.lastrowid

    # Credit the referrer
    if referral_code:
        cursor.execute(
            "UPDATE users SET credits = credits + 10 WHERE referral_code = ?",
            (referral_code,),
        )
        conn.commit()

    conn.close()
    return {"id": user_id, "username": username}


def delete_user(user_id):
    """Remove a user account and associated data."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    conn.close()


def list_users():
    """Return all users. Used by the admin endpoint."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
