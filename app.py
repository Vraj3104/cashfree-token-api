import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CASHFREE_APP_ID = os.environ.get("CASHFREE_APP_ID")
CASHFREE_SECRET_KEY = os.environ.get("CASHFREE_SECRET_KEY")
CASHFREE_URL = "https://sandbox.cashfree.com/pg/orders"

@app.route("/")
def home():
    return "Cashfree Token Generator API is live!"

@app.route("/create_order", methods=["POST"])
def create_order():
    data = request.json
    headers = {
        "Content-Type": "application/json",
        "x-client-id": CASHFREE_APP_ID,
        "x-client-secret": CASHFREE_SECRET_KEY
    }

    response = requests.post(CASHFREE_URL, json=data, headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
