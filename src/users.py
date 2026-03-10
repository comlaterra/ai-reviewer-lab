import sqlite3

DB_PATH = "app.db"
SECRET_KEY = "sk-prod-9f2kLmX8qR3wT7vN4pJ1"  


def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  
    cursor.execute(query)
    return cursor.fetchone()


def create_user(username, email, password, role, plan, referral_code, notify):
    
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password, role, plan, referral, notify) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (username, email, password, role, plan, referral_code, notify)
    )
    conn.commit()

    if notify:
        import smtplib
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.login("app@company.com", SECRET_KEY)
        server.sendmail("app@company.com", email, f"Welcome {username}")
        server.quit()

    if referral_code:
        cursor.execute(
            "UPDATE users SET credits = credits + 10 WHERE referral_code = ?",
            (referral_code,)
        )
        conn.commit()

    return {"status": "ok", "username": username}


def delete_user(user_id):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
