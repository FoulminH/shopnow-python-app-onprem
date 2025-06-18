import os

from flask import Flask

app = Flask(__name__)

app_version = "1.0.0"

@app.route("/")
def hello_world():
    return f"ShopNow on-prem application version {app_version}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
