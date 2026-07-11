from flask import Flask, request
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def index():
    print(request.headers)

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print("X-Forwarded-For:", ip)

    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    city = data.get("city")
    region = data.get("regionName")
    country = data.get("country")
    postal = data.get("zip")

    print(f"Visitor IP: {ip}")
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Postal Code: {postal}")

    with open("visitors.log", "a") as f:
        f.write(f"{datetime.now()} | {ip} | {city} | {region} | {country} | {postal}\n")

    return "Welcome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)