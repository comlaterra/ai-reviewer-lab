from flask import Flask, request, jsonify
from users import get_user, create_user, delete_user
from payments import charge_customer

app = Flask(__name__)


@app.route("/user/<user_id>", methods=["GET"])
def fetch_user(user_id):
    try:
        user = get_user(user_id)  
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  


@app.route("/user", methods=["POST"])
def register():
    data = request.json
    result = create_user(
        data["username"],
        data["email"],
        data["password"],
        data.get("role", "user"),
        data.get("plan", "free"),
        data.get("referral_code"),
        data.get("notify", True)
    )
    return jsonify(result)


@app.route("/user/<user_id>", methods=["DELETE"])
def remove_user(user_id):
    
    delete_user(user_id)
    return jsonify({"status": "deleted"})


@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    
    
    result = charge_customer(data["customer_id"], data["amount"])
    return jsonify(result)


@app.route("/admin/users", methods=["GET"])
def list_all_users():
    
    import sqlite3
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())


if __name__ == "__main__":
    app.run(debug=True)  
