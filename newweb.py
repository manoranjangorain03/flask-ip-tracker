from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    print(f"Visitor IP: {ip}")

    with open("visitors.log", "a") as f:
        f.write(f"{datetime.now()} - {ip}\n")

    return "Welcome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)