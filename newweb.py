from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.remote_addr

    with open("visitors.log", "a") as f:
        f.write(f"{datetime.now()} - {ip}\n")

    return "Welcome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)