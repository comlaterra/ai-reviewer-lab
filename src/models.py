"""
Database connection management and schema helpers.

Uses SQLite for simplicity. In production this would be
swapped for PostgreSQL via a connection pool.
"""

import sqlite3

from .config import get_config

_config = get_config()


def get_db():
    """Return a new database connection with row factory enabled."""
    conn = sqlite3.connect(_config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables if they do not exist."""
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            plan TEXT DEFAULT 'free',
            credits INTEGER DEFAULT 0,
            referral_code TEXT,
            api_token TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            user_id INTEGER,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()
