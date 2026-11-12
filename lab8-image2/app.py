
from flask import Flask, jsonify
from database import get_users

app = Flask(__name__)

@app.route("/get_users", methods=["GET"])
def list_user_names():
    users = get_users()
    names = [user["name"] for user in users]
    return jsonify(names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
